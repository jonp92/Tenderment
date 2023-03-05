from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PrintDetail import PrintDetail
from .. import Print
from ..PrintSummary_Edit import PrintSummary_Edit
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
    Print().repeating_panel_1.item_template = PrintSummary_Edit
    #get_open_form().column_panel_2.add_component(PrintSummary_Edit())


    
      


