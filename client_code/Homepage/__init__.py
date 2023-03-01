from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .PrintSummary import PrintSummary

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    user = anvil.users.login_with_form()
    authenticated = anvil.server.call('is_authenticated')
    self.user = anvil.users.get_user()
    if authenticated is True:
      self.repeating_panel_1.item_template = PrintSummary
      self.repeating_panel = RepeatingPanel()
      self.repeating_panel_1.items = app_tables.images.search()
    else:
      pass

    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def open_prints(self):
    self.ticket_form_open = True
    self.current_form = ItemTemplate1
    self.add_component(self.current_form, slot="default")
    

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






