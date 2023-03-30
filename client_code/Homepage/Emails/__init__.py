from ._anvil_designer import EmailsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Emails(EmailsTemplate):
  def __init__(self, **properties):
    email_data = self.get_email_data()
    self.item = email_data.search()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def get_email_data(self, **event_args):
    return anvil.server.call('get_email_data')
  
  def delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Step through each template form (row) in the repeating panel.
    for r in self.repeating_panel_1.get_components():
    # Step through all the components that make up the row.
      for c in r.get_components():
        if type(c) is CheckBox:
          if c.checked == True:
            r.item.delete()
    email_data = self.get_email_data()
    self.item = email_data
    self.refresh_data_bindings()
    


