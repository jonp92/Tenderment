from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .print_chooser import print_chooser
from .slice_confirm import slice_confirm
from .slice_options import slice_options


class Upload(UploadTemplate):
  def __init__(self, **properties):
    self.uploaded_file = 'None'
    self.image_1.source = anvil.server.get_app_origin() + "/_/theme/tcicon.png"
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file.name.endswith('.gcode'):
      self.png, uploaded_file = anvil.server.call('find_png', file, file.name)
      self.image_1.source = self.png
      self.uploaded_file = uploaded_file
      if self.uploaded_file == "File Already Exist":
        Notification(uploaded_file).show()
      else:
        Notification(uploaded_file, title="File Uploaded Successfully").show()
      self.refresh_data_bindings()
      self.file_loader_1.clear()
    elif file.name.endswith('.stl'):
      #anvil.server.call('upload_stl', file, file.name)
      #self.uploaded_file = file.name
      #self.refresh_data_bindings()
      #self.file_loader_1.clear()
      #alert(print_chooser(file.name), large=True)
      filename = anvil.server.call('upload_stl', file, file.name)
      self.item['quality'] = '0.24mm_FAST_@CREALITY'
      self.item['filament_type'] = 'Inland_PLA+'
      self.item['infill'] = '10%'
      slice_stl = alert(slice_options(item=self.item), title=filename, large=True, buttons=[("Slice", True), ("Cancel", False)])
      if slice_stl:
        self.output_name, self.fileName, self.png, self.filament_type, self.filament_used, self.printing_time, self.cost = anvil.server.call('slice', file.name, self.item['quality'], self.item['filament_type'], self.item['infill'])
        alert(slice_confirm(self.output_name, self.fileName, self.png, self.filament_type, self.filament_used, self.printing_time, self.cost), large=True)
      else:
        anvil.server.call('delete_stl', file.name)
      self.refresh_data_bindings()
      self.file_loader_1.clear()
    else:
      raise Exception('Only .STL or .GCODE files are supported here.')
      
      

