from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PrintDetail import PrintDetail
from .. import Print

class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
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
    get_open_form().column_panel_2.clear()
    get_open_form().column_panel_2.add_component(Print())
    self.refresh_data_bindings()
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True
    
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def update_print_table(self):
    anvil.server.call('update_print_data', self.item['id'], self.text_box_1.text, self.text_box_2.text,
                     self.item['time'], self.item['cost'], self.item['weight'], self.item['status'])




    
      


