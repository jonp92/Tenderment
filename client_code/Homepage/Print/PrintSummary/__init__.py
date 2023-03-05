from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PrintDetail import PrintDetail
from .. import Print
class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_details_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(PrintDetail(self.item.get_id()), large=True,
                        buttons=[("Save", True), ("Cancel", False)])
    if save_clicked:
      anvil.server.call('update_print_data', PrintDetail(self.item))
      Print().refresh_prints()


