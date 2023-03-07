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
    user = anvil.users.login_with_form()
    self.authenticated = anvil.server.call('is_authenticated')
    self.user = anvil.users.get_user()
    self.version = "v0.7.1"
    self.data = [
      {
        'time': r['time'],
        'cost': r['cost'],
        'weight':r['weight']
      }
      for r in anvil.server.call('get_prints', 'No', "")
    ]
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.data[1:])
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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form()

  def link_logoff_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    anvil.users.login_with_form()

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Homepage')

  def link_upload_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      get_open_form().column_panel_2.clear()
      self.column_panel_2.add_component(Upload())
    else:
      pass

  def link_orders_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      get_open_form().column_panel_2.clear()
      self.column_panel_2.add_component(Orders())
    else:
      pass

  def link_inventory_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      get_open_form().column_panel_2.clear()
      self.column_panel_2.add_component(Inventory())
    else:
      pass

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass











