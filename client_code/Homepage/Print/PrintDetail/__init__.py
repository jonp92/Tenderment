from ._anvil_designer import PrintDetailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PrintDetail(PrintDetailTemplate):
  def __init__(self, item_id, **properties):
    self.item = anvil.server.call('get_print_by_id', item_id)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
