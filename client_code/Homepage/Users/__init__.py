from ._anvil_designer import UsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Users(UsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.repeating_panel_users_data.set_event_handler('x-refresh-prints', self.get_users)
    self.init_components(**properties)
    self.get_users() 
    # Any code you write here will run before the form opens.
    
  def get_users(self, **event_args):
    self.repeating_panel_users_data.items = anvil.server.call('get_users')