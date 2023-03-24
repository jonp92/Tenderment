import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def authorization():
  if anvil.users.get_user()['role'] == 'admin' or 'superadmin':
    return True
  else:
    return False

@anvil.server.callable
def get_users():
  return app_tables.users.search()  

@anvil.server.callable(require_user=authorization())
def edit_user(id, first_name, last_name, email, role, enabled, confirmed_email, password):
  import bcrypt
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  user_row = app_tables.users.get_by_id(id)
  user_row.update(first_name=first_name, last_name = last_name, email = email, role = role, enabled = enabled, confirmed_email = confirmed_email, password_hash = password_hash.decode('utf-8'))

@anvil.server.callable(require_user=authorization())
def add_user(first_name, last_name, email, role, enabled, confirmed_email, password):
  import bcrypt
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

@anvil.server.callable(require_user=authorization())
def delete_user(id):
  user_row = app_tables.users.get_by_id(id)
  user = user_row['first_name'] + " " + user_row['last_name']
  user_row.delete()

@anvil.server.callable
def user_role():
  return anvil.users.get_user()['role']


