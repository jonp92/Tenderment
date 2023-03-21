from ._anvil_designer import slice_confirmTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class slice_confirm(slice_confirmTemplate):
  def __init__(self, output_name, fileName, png, **properties):
    # Set Form properties and Data Bindings.
    self.link_title.text = output_name
    self.image_thumbnail.source = png
    self.filename - fileName
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
