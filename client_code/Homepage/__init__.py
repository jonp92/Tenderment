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

def error_handler(err):
  alert(str(err), title="An error has occurred", large=True, dismissible=False)

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    self.user = anvil.users.get_user()
    set_default_error_handling(error_handler)
    self.item['version'] = "v0.5.8"
    #self.form_session = anvil.server.call('get_form_session')
    #self.print_count = anvil.server.call('count_prints')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if self.user['role'] == 'user':
      self.column_panel_2.clear()
      self.link_home.visible = False
      self.link_settings.visible = False
      self.link_users.visible = False
      self.link_orders.visible = False
      self.link_prints.visible = False
      self.link_inventory.visible = False
      self.column_panel_2.add_component(Upload())
    
    #if self.form_session:
      #self.column_panel_2.clear()
      #self.column_panel_2.add_component(self.form_session)
    self.plot_1.data = anvil.server.call('plot_prints_pie')
    self.label_print_count.text = anvil.server.call('count_prints')
    
  def link_current_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    
  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    #anvil.server.call('set_form_session', 'Print(), full_width_row=True')
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Print(), full_width_row=True)

  def link_logoff_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form('Login')   

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Homepage')

  def link_upload_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Upload())

  def link_orders_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Orders())

  def link_inventory_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Inventory())

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def link_settings_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Settings(item=self.item))

  def link_users_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Users(), full_width_row=True)




  










