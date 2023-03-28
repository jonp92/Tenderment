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
    if self.item['selected_table'] == 'Infill':
      columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in app_tables.infill.list_columns()]
      self.data_grid_table.columns = columns
      self.repeating_panel_table.item_template = Infill
      self.repeating_panel_table.items = app_tables.infill.search()
      self.data_grid_table.columns = self.data_grid_table.columns
      self.refresh_data_bindings()
    elif self.item['selected_table'] == 'Quality':
      columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in app_tables.quality.list_columns()]
      self.data_grid_table.columns = columns
      self.repeating_panel_table.item_template = Quality
      self.repeating_panel_table.items = app_tables.quality.search()
      self.data_grid_table.columns = self.data_grid_table.columns
      self.refresh_data_bindings()
    elif self.item['selected_table'] == 'Printers':
      columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in app_tables.printers.list_columns()]
      self.data_grid_table.columns = columns
      self.repeating_panel_table.item_template = Printers
      self.repeating_panel_table.items = app_tables.printers.search()      
      self.data_grid_table.columns = self.data_grid_table.columns
      self.refresh_data_bindings()
    elif self.item['selected_table'] == 'STLs':
      client_table = anvil.server.call('get_stl_data')
      columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in client_table.list_columns()]
      self.data_grid_table.columns = columns
      self.repeating_panel_table.item_template = TableView
      self.repeating_panel_table.items = client_table.search()
      self.data_grid_table.columns = self.data_grid_table.columns
      self.refresh_data_bindings()
    elif self.item['selected_table'] == 'Settings':
      columns = [{'id': d['id'], 'title': d['name'], 'data_key': d['name']} for d in app_tables.settings.list_columns()]
      self.data_grid_table.columns = columns
      self.repeating_panel_table.item_template = Settings
      self.repeating_panel_table.items = app_tables.settings.search()
      self.data_grid_table.columns = self.data_grid_table.columns
      self.refresh_data_bindings()
    
  def refresh_stl_table(self, **event_args):
    client_table = anvil.server.call('get_stl_data')
    self.repeating_panel_table.items = client_table.search()
    self.refresh_data_bindings()

  def button_add_row_click(self, **event_args):
    self.item['selected_value'] = self.drop_down_selected_table.selected_value
    self.repeating_panel_table.item_template = 
    self.repeating_panel_table.items = self.item
    self.refresh_data_bindings()

  def new_row_added(self, **event_args):
    self.repeating_panel_table.item_template = TableView
    self.refresh_data_bindings()
    