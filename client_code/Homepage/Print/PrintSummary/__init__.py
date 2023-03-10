from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.media
from ..PrintDetail import PrintDetail

class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    user_role = anvil.server.call('user_role')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #  Any code you write here will run before the form opens.

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
      self.parent.raise_event('x-refresh-prints')
      self.data_row_panel_edit.visible = False
      self.data_row_panel_view.visible = True
    else:
      self.parent.raise_event('x-refresh-prints')
      
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
    anvil.media.download(media)

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(user_role)
    if anvil.server.call('user_role') == "user":
      alert("You are not authorized to delete Prints")
    else:
      delete_clicked = alert(f"Are you sure you want to DELETE {self.text_box_name.text}?", title="Delete Table Row", buttons=[("Delete", True), ("Cancel", False)])
      if delete_clicked:
        anvil.server.call('delete_prints_row', self.item)
        self.parent.raise_event('x-refresh-prints')
        self.data_row_panel_edit.visible = False
        self.data_row_panel_view.visible = True  

  def image_1_mouse_down(self, x, y, button, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    print_copy = dict(self.item)
    save_clicked = alert(PrintDetail(item=print_copy), large=True, buttons=[("Close", False)])
      
      










    
      


