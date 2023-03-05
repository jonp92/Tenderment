from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PrintDetail import PrintDetail
from .. import Print
from ..PrintSummary_Edit import PrintSummary_Edit
class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.        
    self.print_id = None
    self.print_name = None
    self.print_uploaded = None
    self.print_time = None
    self.print_cost = None
    self.print_weight = None
    self.print_status = None
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.update_print_table()
    self.refresh_data_bindings()
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True
    
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def update_print_table(self):
    anvil.server.call('update_print_data', self.item['id'], self.print_name, self.item['uploaded'],
                     self.item['time'], self.item['cost'], self.item['weight'], self.item['status'])




    
      


