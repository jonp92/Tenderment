from ._anvil_designer import EmailsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Emails(EmailsTemplate):
  def __init__(self, **properties):
    email_data = anvil.server.call('get_email_data')
    self.item = email_data.search()
    self.item['attachments'] = anvil.server.call('get_attachments')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
