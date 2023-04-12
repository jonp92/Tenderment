from ._anvil_designer import AddRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .... import globals

class AddRow(AddRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.columns = globals.selected_table.list_columns()
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    components = self.get_components()
    print(components)
    for item in self.columns:
      column_name = item['name']
      column_data = self.text_box_new_row.text
      globals.selected_table.add_row(**{column_name: column_data})
    self.parent.raise_event('x-new-row')

