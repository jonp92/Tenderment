from ._anvil_designer import NotesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Notes(NotesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.set_event_handler('x-refresh-prints', self.refresh_notes)
    # Any code you write here will run before the form opens.
    self.refresh_notes()
  def refresh_notes(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call('get_notes', self.item)
