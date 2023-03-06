from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.media
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
    save_clicked = alert(f"Are you sure you want to update {self.text_box_name.text}?", title="Update Table Info", buttons=[("Save", True), ("Cancel", False)])
    if save_clicked:
      self.update_print_table()
      get_open_form().column_panel_2.clear()
      get_open_form().column_panel_2.add_component(Print())
      self.refresh_data_bindings()
      self.data_row_panel_edit.visible = False
      self.data_row_panel_view.visible = True
    else:
      self.data_row_panel_edit.visible = False
      self.data_row_panel_view.visible = True
    
    
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def update_print_table(self):
    anvil.server.call('update_print_data', self.item['id'], self.text_box_name.text, self.text_box_uploaded.text,
                     self.text_box_time.text, self.text_box_cost.text, self.text_box_weight.text, self.drop_down_status_edit.selected_value)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True

  def drop_down_status_edit_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_download_click(self, **event_args):
    """This method is called when the button is clicked"""
    media = anvil.server.call('get_gcode_download', self.item.get_id())
    anvil.media.download(media, )







    
      


