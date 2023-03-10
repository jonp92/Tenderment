import anvil.users
import anvil.server

@anvil.server.callable
def user_role():
  return anvil.users.get_user()['role']