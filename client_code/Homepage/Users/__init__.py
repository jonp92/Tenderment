from ._anvil_designer import UsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
import time
from anvil.tables import app_tables
from .AddUser import AddUser

class Users(UsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.repeating_panel_users_data.set_event_handler('x-refresh-users', self.get_users)
    #self.drop_down_role.items = anvil.server.call('get_roles')
    self.init_components(**properties)
    self.get_users() 
    # Any code you write here will run before the form opens.
    
  def get_users(self, **event_args):
    self.item = anvil.server.call('get_users')

  def button_add_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    #self.repeating_panel_users_data.visible = False
    #self.data_row_panel_new_user.visible = True
    #self.button_add_user.visible = False
    save = alert(AddUser(), large=True, buttons=[])
    if save:
      self.get_users()
      self.refresh_data_bindings()
    else:
      pass
      
  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_new_user.visible = False
    self.repeating_panel_users_data.visible = True
    self.button_add_user.visible = True

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    with Notification('Added User ' + self.text_box_first_name.text + ' ' + self.text_box_last_name.text, title='User Added', style='success'):
      anvil.server.call('add_user', self.text_box_first_name.text, self.text_box_last_name.text, self.text_box_email.text, self.drop_down_role.selected_value, self.check_box_enabled.checked, self.check_box_confirmed_email.checked, self.text_box_password.text)
      self.get_users()
      self.refresh_data_bindings()
      self.data_row_panel_new_user.visible = False
      self.repeating_panel_users_data.visible = True
      self.button_add_user.visible = True


      
