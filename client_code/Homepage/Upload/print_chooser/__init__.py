from ._anvil_designer import print_chooserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class print_chooser(print_chooserTemplate):
  def __init__(self, filename, **properties):
    self.item = anvil.server.call('get_prints', 'No', "")
    self.names = [r['name'] for r in self.item]
    self.thumbs = [r['media_object'] for r in self.item]
    self.filename = filename
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_print_name.items = self.names

    # Any code you write here will run before the form opens.

  def drop_down_print_name_change(self, **event_args):
    """This method is called when an item is selected"""
    #print_name = self.drop_down_print_name.selected_value
    self.print_row = anvil.server.call('get_print_by_name', self.drop_down_print_name.selected_value)
    self.image_print_thumbnail.visible = True
    self.image_print_thumbnail.source = self.print_row['media_object']

  def button_link_print_click(self, **event_args):
    """This method is called when the button is clicked"""
    #print_row = anvil.server.call('get_print_by_name', self.drop_down_print_name.selected_value)
    anvil.server.call('link_stl_to_print', self.print_row, self.filename)
    self.label_link.visible = True
    self.label_link.text = self.filename + " has been linked to " + self.print_row['name'] +"."
    
    


