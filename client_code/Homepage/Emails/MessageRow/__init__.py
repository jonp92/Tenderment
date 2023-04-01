from ._anvil_designer import MessageRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ThumbnailPop import ThumbnailPop

class MessageRow(MessageRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.attachments = anvil.server.call('get_attachments', self.item)
    if self.attachments:
      self.image_1.source = self.attachments
    #self.quill_html.set_html('html', sanitize=True)

    # Any code you write here will run before the form opens.

  def image_1_mouse_down(self, x, y, button, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    alert(ThumbnailPop(self.attachments), large=True, buttons=[])





  
