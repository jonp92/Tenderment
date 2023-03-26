from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.users

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    anvil.server.call('set_form_session', 'login')
    open_form('Homepage')

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    if anvil.users.get_user():
      open_form('Homepage')