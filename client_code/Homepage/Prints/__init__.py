from ._anvil_designer import PrintsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import PrintSummary
from ... import Homepage

class Prints(PrintsTemplate):
  def __init__(self, **properties):
    self.selected_status = 'All'
    self.selected_sort = 'None'
    self.number_rows = '4'
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.prints.search()
    # Any code you write here will run before the form opens.
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.change_status_filter(self.selected_status)

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.selected_sort == 'None':
      self.repeating_panel_1.items = app_tables.prints.search()
    else:
      self.repeating_panel_1.items = sorted([r for r in self.repeating_panel_1.items], key = lambda x: x[self.selected_sort])

  def drop_down_rows_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.number_rows == 'All':
      self.data_grid_1.rows_per_page = 0
      self.refresh_data_bindings()
    else:
      self.refresh_data_bindings()

  def change_status_filter(self, status):
    if status == 'All':
      self.repeating_panel_1.items = app_tables.prints.search()
    else:
      self.repeating_panel_1.items = app_tables.prints.search(status=status)

  def refresh_prints(self):
    self.refresh_data_bindings()


