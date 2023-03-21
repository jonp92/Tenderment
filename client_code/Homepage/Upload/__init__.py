from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .print_chooser import print_chooser


class Upload(UploadTemplate):
  def __init__(self, **properties):
    self.uploaded_file = 'None'
    self.image_1.source = anvil.server.get_app_origin() + "/_/theme/tcicon.png"
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if self.drop_down_file_type.selected_value == ".gcode":
      self.png, uploaded_file = anvil.server.call('find_png', file, file.name)
      self.image_1.source = self.png
      self.uploaded_file = uploaded_file
      if self.uploaded_file == "File Already Exist":
        Notification(uploaded_file).show()
      else:
        Notification(uploaded_file, title="File Uploaded Successfully").show()
      self.refresh_data_bindings()
      self.file_loader_1.clear()
    else:
      anvil.server.call('upload_stl', file, file.name)
      self.uploaded_file = file.name
      self.refresh_data_bindings()
      self.file_loader_1.clear()
      alert(print_chooser(file.name), large=True)
      

