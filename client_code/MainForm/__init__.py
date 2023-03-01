from ._anvil_designer import MainFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
from datetime import datetime
class MainForm(MainFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.uploaded_file = None
    self.gcode = None
    self.weight = None
    self.price = None
    self.time = None
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.png, price, weight, time = anvil.server.call('find_png', file, file.name)
    #if file.name not in [r['name'] for r in app_tables.images.search()]:
      #self.png_table = app_tables.images.add_row(name=file.name, media_object=self.png)
    #self.png_table = app_tables.images.add_row(name=file.name + "-" + datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p") , media_object=self.png)
    self.image_1.source = self.png
    if price == 'Not Found':
      self.price = price
    else:
      self.price = f'${price}'
    if weight == 'Not Found':
      self.weight = weight
    else:
      self.weight = f'{weight} g'
    if time == 'Not Found':
      self.time = time
    else:
      self.time = f'{time}'
    self.filename = file.name
    self.uploaded_file = file.name
    self.refresh_data_bindings()
    FileLoader().clear()
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.check_box_1.checked == True:
      download_row = app_tables.images.get(name='self.gcode')
    else:
      download_row = app_tables.images.get(name=self.filename)
    anvil.media.download(download_row['media_object'])

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.check_box_1.checked == True:
      self.text_area_1.visible = True
      self.cut_thumb.visible = True
      self.file_loader_1.visible = False
    elif self.check_box_1.checked == False:
      self.text_area_1.visible = False
      self.cut_thumb.visible = False
      self.file_loader_1.visible = True      

  def cut_thumb_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.png = anvil.server.call('find_png_gcode', self.gcode, 'self.gcode')
    self.image_1.source = self.png

      
      


