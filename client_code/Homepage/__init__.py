from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Prints import Prints
from .Prints.PrintSummary import PrintSummary

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    user = anvil.users.login_with_form()
    self.authenticated = anvil.server.call('is_authenticated')
    self.user = anvil.users.get_user()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.remove_from_parent()
    # Any code you write here will run before the form opens.
  
  def open_prints(self):
    if self.authenticated is True:
      get_open_form().column_panel_2.clear()
      self.add_component(Prints())
    else:
      pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()
    pass

  def link_prints_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.open_prints()

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






