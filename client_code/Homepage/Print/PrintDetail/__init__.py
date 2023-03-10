from ._anvil_designer import PrintDetailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..Notes import Notes
from anvil.tables import app_tables
from ... import Homepage

class PrintDetail(PrintDetailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('add_note', self.item, self.text_area_1.text)
    self.text_area_1.text = None

  def text_area_1_lost_focus(self, **event_args):
    """This method is called when the text area loses focus"""
    pass

  def button_open_notes_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(Notes(item=self.item), large=True)



    
    

  
    




