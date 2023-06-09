from ._anvil_designer import PrintTemplate
from anvil import *
import anvil.server

class Print(PrintTemplate):
  def __init__(self, **properties):
    self.selected_status = 'All'
    self.selected_sort = 'None'
    self.number_rows = '4'
    self.repeating_panel_1.set_event_handler('x-refresh-prints', self.refresh_prints)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_prints()
    # Any code you write here will run before the form opens.

  def refresh_prints(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('get_prints', 'No', "")
    
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.change_status_filter(self.selected_status)

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.selected_sort == 'None':
      self.repeating_panel_1.items = anvil.server.call('get_prints', 'No', status="")
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
      self.repeating_panel_1.items = anvil.server.call('get_prints', 'No', status="")
    else:
      self.repeating_panel_1.items = anvil.server.call('get_prints', 'Yes', status=status)
      




