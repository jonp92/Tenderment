from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    delete_clicked = alert("Are you sure you want to delete this note?", buttons=[("Delete", True),("Cancel", False)])
    if delete_clicked:
     anvil.server.call('delete_note', self.item)
     self.parent.raise_event('x-refresh-prints')

