import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_users():
  return app_tables.users.search()  

@anvil.server.callable
def save_user(id, first_name, last_name, email, role, enabled, confirmed_email, password_hash):
  user_row = app_tables.users.get_by_id(id)
  user_row.update(first_name=first_name, last_name = last_name, email = email, role = role, enabled = enabled, confirmed_email = confirmed_email, password_hash = password_hash)