from ._anvil_designer import AddUserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddUser(AddUserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_role.items = anvil.server.call('get_roles')
    self.item['role'] = self.drop_down_role.selected_value
    print(self.item['role'])
    # Any code you write here will run before the form opens.

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event('x-close-alert', value=False)

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    with Notification('Added User ' + self.item['first_name'] + ' ' + self.item['last_name']):
      anvil.server.call('add_user', self.item['first_name'], self.item['last_name'], self.item['email'], self.item['role'], self.item['enabled'], self.item['confirmed_email'], self.item['password'])
      self.raise_event('x-close-alert', value=True)

