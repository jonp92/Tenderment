from ._anvil_designer import OrdersTemplate
from anvil import *
import anvil.server

class Orders(OrdersTemplate):
  def __init__(self, **properties):
    url = f"/commerce/orders"
    self.order = anvil.server.call('get_sqdata', url)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
