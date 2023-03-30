from ._anvil_designer import ComposeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Compose(ComposeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_send_click(self, **event_args):
    """This method is called when the button is clicked"""
    with Notification('Email sent to ' + self.item['to'], title='Email Sent!', style='success'):
      attachment = app_tables.outgoing_attachments.get()
      if attachment:
        anvil.server.call('send_email', self.item['to'], self.item['subject'], self.item['msg_body'], attachment['attachment'])
      else:
        attachment = None
        anvil.server.call('send_email', self.item['to'], self.item['subject'], self.item['msg_body'], attachment)
    self.raise_event('x-close-alert', value=True)

  def file_loader_attach_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    app_tables.outgoing_attachments.add_row(attachment=file)

    
    
    
