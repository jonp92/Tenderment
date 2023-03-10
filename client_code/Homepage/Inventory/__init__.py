from ._anvil_designer import InventoryTemplate
from anvil import *
import anvil.server
from .InventorySettings import InventorySettings

class Inventory(InventoryTemplate):
  def __init__(self, **properties):
    self.item = anvil.server.call('get_wix_products_table')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if get_open_form().user['role'] == "superadmin":
      self.button_settings.visible = True
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('set_wix_products', f"stores/v1/products/query")

  def button_settings_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(InventorySettings(item=self.item), large=True)

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    



