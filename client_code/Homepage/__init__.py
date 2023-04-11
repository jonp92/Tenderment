from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import anvil.server
from .Print import Print
from .Upload import Upload
from .Orders import Orders
from .Inventory import Inventory
from .Settings import Settings
from .Users import Users
from .TableExplorer import TableExplorer
from .Emails import Emails
from .. import globals
def error_handler(err):
  alert(str(err), title="An error has occurred", large=True, dismissible=False)

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    globals.initial_install()
    self.user = anvil.users.get_user()
    set_default_error_handling(error_handler)
    self.item['version'] = "v0.5.8"
    self.form_session = anvil.server.call('get_form_session')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.session_orientation()

  def session_orientation(self, **event_args):
    if self.user['role'] == 'user':
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Upload())
      self.link_home.visible = False
      self.link_settings.visible = False
      self.link_users.visible = False
      self.link_orders.visible = False
      self.link_prints.visible = False
      self.link_inventory.visible = False
    if not self.form_session or self.form_session == 'Homepage':
      self.form_session = 'Homepage'
      self.plot_1.data, self.label_print_count.text = anvil.server.call('plot_prints_pie')
    else:
      forms = {'Print': {'form': Print, 'full_width': True},
              'Inventory': {'form': Inventory, 'full_width': True},
              'Settings': {'form': Settings, 'full_width': True},
              'Upload': {'form': Upload, 'full_width': True},
              'Users': {'form': Users, 'full_width': False},
              'TableExplorer': {'form': TableExplorer, 'full_width': False},
              'Emails': {'form': Emails, 'full_width': False}}
      if self.form_session in forms:
          form_info = forms[self.form_session]
          self.column_panel_2.clear()
          self.column_panel_2.add_component(form_info['form'](), full_width_row=form_info['full_width'])

  def link_current_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    
  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Print')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Print(), full_width_row=True)

  def link_logoff_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Login')
    anvil.users.logout()
    open_form('Login')   

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Homepage')
    open_form('Homepage')

  def link_upload_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Upload')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Upload())

  def link_orders_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Orders')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Orders())

  def link_inventory_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Inventory')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Inventory())

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def link_settings_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Settings')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Settings(item=self.item))

  def link_users_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Users')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Users(), full_width_row=True)

  def link_table_explorer_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'TableExplorer')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(TableExplorer(), full_width_row=True)

  def link_email_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('set_form_session', 'Emails')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Emails(), full_width_row=True)






  










