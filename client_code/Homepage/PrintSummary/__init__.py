from ._anvil_designer import PrintSummaryTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PrintSummary(PrintSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.item['name'])
    self.filename.text = self.item['name']
    
    # Any code you write here will run before the form opens.

