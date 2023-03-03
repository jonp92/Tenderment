from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Prints import Prints
from .Prints.PrintSummary import PrintSummary
from .Upload import Upload

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    user = anvil.users.login_with_form()
    self.authenticated = anvil.server.call('is_authenticated')
    self.user = anvil.users.get_user()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
  
  def link_current_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    
  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    if self.authenticated is True:
      self.column_panel_2.clear()
      self.column_panel_2.add_component(Prints())
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









