from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import anvil.server
from .Print import Print
from .Upload import Upload
from .Orders import Orders
from .Inventory import Inventory
def error_handler(err):
  alert(str(err), title="An error has occurred")

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    self.user = anvil.users.login_with_form()
    set_default_error_handling(error_handler)
    self.version = "v0.5.5"
    #self.print_count = anvil.server.call('count_prints')
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.plot_1.data = anvil.server.call('plot_prints_pie')
    self.label_print_count.text = anvil.server.call('count_prints')
    
  def link_current_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    
  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_2.add_component(Print())

  def link_logoff_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_2.clear()
    self.column_panel_1.clear()
    self.link_current_user.clear()
    anvil.users.logout()
    anvil.users.login_with_form()
    open_form('Homepage')   

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


  










