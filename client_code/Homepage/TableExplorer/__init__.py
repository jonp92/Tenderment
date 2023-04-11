from ._anvil_designer import TableExplorerTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Infill import Infill
from .Printers import Printers
from .Quality import Quality
from .Settings import Settings
from .TableView import TableView
from .AddRow import AddRow
from .Email_Table import Email_Table
from ... import globals
class TableExplorer(TableExplorerTemplate):
  def __init__(self, **properties):
    self.repeating_panel_table.set_event_handler('x-refresh-stl-table', self.refresh_stl_table)
    self.repeating_panel_table.set_event_handler('x-new-row', self.new_row_added)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def drop_down_selected_table_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.data_grid_table.visible == False:
      self.data_grid_table.visible = True
    self.repeating_panel_table.items = None
    tables = {'Infill': {'table': app_tables.infill, 'template': Infill},
          'Quality': {'table': app_tables.quality, 'template': Quality},
          'Printers': {'table': app_tables.printers, 'template': Printers},
          'STLs': {'table': None, 'template': TableView, 'func': 'get_stl_data'},
          'Settings': {'table': app_tables.settings, 'template': Settings},
          'Emails': {'table': None, 'template': Email_Table, 'func': 'get_email_data'}}
    if self.item['selected_table'] in tables:
        table_info = tables[self.item['selected_table']]
        if table_info['table'] is not None:
            columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in table_info['table'].list_columns()]
            self.data_grid_table.columns = columns
            self.repeating_panel_table.item_template = table_info['template']
            self.repeating_panel_table.items = table_info['table'].search()
            globals.selected_table = table_info['table']
        else:
            client_table = anvil.server.call(table_info['func'])
            columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in client_table.list_columns()]
            self.data_grid_table.columns = columns
            self.repeating_panel_table.item_template = table_info['template']
            self.repeating_panel_table.items = client_table.search()
        self.data_grid_table.columns = self.data_grid_table.columns
        self.refresh_data_bindings()    
    
  def refresh_stl_table(self, **event_args):
    client_table = anvil.server.call('get_stl_data')
    self.repeating_panel_table.items = client_table.search()
    self.refresh_data_bindings()

  def button_add_row_click(self, **event_args):
    self.repeating_panel_table.item_template = AddRow
    self.repeating_panel_table.items = self.item
    self.refresh_data_bindings()

  def new_row_added(self, **event_args):
    self.repeating_panel_table.item_template = TableView
    self.refresh_data_bindings()
    