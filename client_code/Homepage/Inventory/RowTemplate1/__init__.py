from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Inventory
class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.thumbnail_url = None
    self.quantity = None
    self.init_components(**properties)
    #self.quantity = self.item['stock']['quantity']
    #self.thumbnail_url = self.item['media']['mainMedia']['thumbnail']['url']
    self.refresh_data_bindings()

    # Any code you write here will run before the form opens.


