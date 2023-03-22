from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.drop_down_printer.selected_value = [r['selected_printer'] for r in app_tables.settings.search()][0]
    self.init_components(**properties)
    self.drop_down_printer.items = self.item['printers']

    # Any code you write here will run before the form opens.

  def Save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_settings', self.item)

