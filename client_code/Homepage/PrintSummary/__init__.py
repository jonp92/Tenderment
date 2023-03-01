from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import Homepage

class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label5.text = self.item['name']
    
    # Any code you write here will run before the form opens.

