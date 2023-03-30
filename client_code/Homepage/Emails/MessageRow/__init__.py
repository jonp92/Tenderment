from ._anvil_designer import MessageRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MessageRow(MessageRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    attachments = anvil.server.call('get_attachments', self.item)
    print(attachments)
    if attachments:
      self.image_1.source = attachments

    # Any code you write here will run before the form opens.




  
