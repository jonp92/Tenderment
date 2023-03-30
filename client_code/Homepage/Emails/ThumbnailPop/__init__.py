from ._anvil_designer import ThumbnailPopTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ThumbnailPop(ThumbnailPopTemplate):
  def __init__(self, image, **properties):
    # Set Form properties and Data Bindings.
    self.image_enlarged.source = image
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
