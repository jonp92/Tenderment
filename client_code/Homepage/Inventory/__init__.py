from ._anvil_designer import InventoryTemplate
from anvil import *
import anvil.server

class Inventory(InventoryTemplate):
  def __init__(self, **properties):
    url = f"/commerce/inventory"
    self.inventory = anvil.server.call('get_sqdata', url)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
