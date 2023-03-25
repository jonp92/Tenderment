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
    self.drop_down_quality.items = [r['quality'] for r in app_tables.quality.search()]
    self.drop_down_filament.items = [r['filament'] for r in app_tables.filament.search()]
    self.drop_down_infill.items = [r['infill'] for r in app_tables.infill.search()]
    self.label_filename.text = filename
    self.item['quality'] = self.drop_down_quality.selected_value
    self.item['filament_type'] = self.drop_down_filament.selected_value
    self.item['infill'] = self.drop_down_infill.selected_value
    # Any code you write here will run before the form opens.

    



