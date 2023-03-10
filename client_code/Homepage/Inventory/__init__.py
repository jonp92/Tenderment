from ._anvil_designer import InventoryTemplate
from anvil import *
import anvil.server

class Inventory(InventoryTemplate):
  def __init__(self, **properties):
    url = f"stores/v1/products/query"
    self.item = anvil.server.call('get_wix_products', url)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if get_open_form().user['email'] == "jonathan@3dmk.xyz":
      self.button_settings.visible = True

  def get_thumbnail_url(self):
    return self.item['media']['mainMedia']['thumbnail']['url']

  def get_quantity(self):
    return self.item['stock']['quantity']    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('set_wix_products', f"stores/v1/products/query")

