from ._anvil_designer import UserSummaryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..UserDetail import UserDetail

class UserSummary(UserSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('edit_user', self.item.get_id(), self.text_box_first_name.text, self.text_box_last_name.text, self.text_box_email.text, self.text_box_role.text, self.check_box_enabled_edit.checked, self.check_box_confirmed_email_edit.checked, self.text_box_password_hash.text)
    self.parent.raise_event('x-refresh-users')
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True

  def button_delete_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    delete_user = alert('Are you sure you want to delete ' + self.item['first_name'] + ' ' + self.item['last_name'])
    if delete_user:
      with Notification('Deleted ' + self.item['first_name'] + ' ' + self.item['last_name'], title='User Deleted', style='danger'):
        anvil.server.call('delete_user', self.item.get_id())
        self.parent.raise_event('x-refresh-users')
        self.data_row_panel_edit.visible = False
        self.data_row_panel_view.visible = True

  def link_first_name_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(UserDetail(item=self.item))




