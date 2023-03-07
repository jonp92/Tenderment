import anvil.users
import anvil.server

@anvil.server.callable
def is_authenticated():
  if anvil.users.get_user():
    authenticated = True
  else:
    authenticated = False
  return authenticated