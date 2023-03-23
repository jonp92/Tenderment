import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt

@anvil.server.callable
def get_users():
  return app_tables.users.search()  

@anvil.server.callable
def edit_user(id, first_name, last_name, email, role, enabled, confirmed_email, password):
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  user_row = app_tables.users.get_by_id(id)
  user_row.update(first_name=first_name, last_name = last_name, email = email, role = role, enabled = enabled, confirmed_email = confirmed_email, password_hash = password_hash.decode('utf-8'))

@anvil.server.callable
def add_user(first_name, last_name, email, role, enabled, confirmed_email, password):
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  app_tables.users.add_row(first_name=first_name, last_name=last_name, email=email, role=role, enabled=enabled, confirmed_email=confirmed_email, password_hash=password_hash.decode('utf-8'))

@anvil.server.callable
def get_roles():
  return [r['role'] for r in app_tables.roles.search()]

@anvil.server.callable
def delete_user(id):
  user_row = app_tables.users.get_by_id(id)
  user = user_row['first_name'] + " " + user_row['last_name']
  user_row.delete()
  