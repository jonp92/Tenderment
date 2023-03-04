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
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_qty(self):
    variantId = self.item['variantId']
    qty = self.item['quantity']
    anvil.server.call('edit_sqqty', variantId, qty)

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.edit_qty()

