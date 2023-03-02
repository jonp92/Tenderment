from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Upload(UploadTemplate):
  def __init__(self, **properties):
    self.uploaded_file = 'None'
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.png = anvil.server.call('find_png', file, file.name)
    self.image_1.source = self.png
    self.filename = file.name
    self.uploaded_file = file.name
    self.refresh_data_bindings()

