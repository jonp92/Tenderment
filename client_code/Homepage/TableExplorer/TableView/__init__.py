from ._anvil_designer import TableViewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class TableView(TableViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.parent.raise_event('x-refresh-stl-table')

