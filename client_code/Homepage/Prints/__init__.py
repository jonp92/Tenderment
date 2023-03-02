from ._anvil_designer import PrintsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from . import PrintSummary

class Prints(PrintsTemplate):
  def __init__(self, **properties):
    self.selected_status = 'All'
    self.selected_sort = 'None'
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.prints.search()

    # Any code you write here will run before the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    print(self.selected_status)

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    print(self.selected_sort)


