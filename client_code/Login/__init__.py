from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.user = anvil.users.get_user()
    self.init_components(**properties)
    if self.user:
      self.visible = False
    else:
      self.visible = True
    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    if self.user:
      open_form('Homepage')
      
  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    anvil.server.call('set_form_session', 'Homepage')
    open_form('Homepage')