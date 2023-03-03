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
    tcicon = anvil.server.get_app_origin() + "/_/theme/tcicon.png"
    self.image_1.source = tcicon
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.png, uploaded_file = anvil.server.call('find_png', file, file.name)
    self.image_1.source = self.png
    self.filename = uploaded_file
    self.uploaded_file = file.name
    self.refresh_data_bindings()

