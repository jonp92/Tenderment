from ._anvil_designer import slice_optionsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class slice_options(slice_optionsTemplate):
  def __init__(self, filename, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_quality.items = [r['quality'] for r in app_tables.static_info.search()]
    self.drop_down_filament.items = [r['filament'] for r in app_tables.static_info.search()]
    self.label_filename.text = filename
    # Any code you write here will run before the form opens.

    



