from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Print import Print, PrintSummary
from .Upload import Upload
from .Orders import Orders
from .Inventory import Inventory

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    self.user = anvil.users.login_with_form()
    self.authenticated = anvil.server.call('is_authenticated')
    #self.user = anvil.users.get_user()
    self.version = "v0.7.1"
    self.print_count = anvil.server.call('count_prints')
    #self.plot_1.data = go.Pie(values=self.print_statues)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def link_current_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    
  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Print())
    else:
      anvil.alert(title='Not Authorized') 

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
    if self.authenticated is True:
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Upload())
    else:
      pass

  def link_orders_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Orders())
    else:
      pass

  def link_inventory_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Inventory())
    else:
      pass

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass











