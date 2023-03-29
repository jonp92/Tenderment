from ._anvil_designer import LogTailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LogTail(LogTailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.text_area_log_data.text = anvil.server.call('tail_log')
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
