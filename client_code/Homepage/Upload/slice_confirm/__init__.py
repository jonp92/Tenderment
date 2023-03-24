from ._anvil_designer import slice_confirmTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class slice_confirm(slice_confirmTemplate):
  def __init__(self, output_name, fileName, png, filament_type, filament_used, printing_time, cost, **properties):
    # Set Form properties and Data Bindings.
    self.link_title.text = fileName
    self.image_thumbnail.source = anvil.server.call('plot_stl', self.item.get_id())
    self.label_filament_type_data.text = filament_type
    self.label_filament_used_data.text = filament_used
    self.label_cost_data.text = cost
    self.label_print_time_data.text = printing_time
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
