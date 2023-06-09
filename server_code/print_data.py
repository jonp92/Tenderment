import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime

now = datetime.datetime.now()
date_string = now.strftime("%Y_%m_%d")
time_string =now.strftime("%H:%M:%S")

def authorization():
  if anvil.users.get_user():
    if anvil.users.get_user()['role'] == 'admin' or 'superadmin':
      return True
    else:
      return False

@anvil.server.callable
def count_unique(list):
  import pandas as pd
  return pd.Series(list).value_counts()

@anvil.server.callable
def get_prints(status_search, status):
  if status_search == 'Yes':
    return app_tables.prints.search(status=status)
  else:
    return app_tables.prints.search()

@anvil.server.callable
def get_print_by_id(id):
  return app_tables.prints.get(id=id)

@anvil.server.callable
def get_print_by_name(name):
  return app_tables.prints.get(name=name)

@anvil.server.callable(require_user=authorization())
def update_print_data(id, name, uploaded, time, cost, weight, status):
  update_row = app_tables.prints.get(id=id)
  update_row.update(name=name, uploaded=uploaded, time=time, cost=float(cost), weight=float(weight), status=status)

@anvil.server.callable(require_user=authorization())
def delete_prints_row(row):
  user_role = anvil.users.get_user()['role']
  if user_role == 'admin' or user_role == 'superadmin':
    row.delete()
  else:
    raise Exception('You are not authorized to delete prints.')

@anvil.server.callable
def add_note(row, notes):
  user = anvil.users.get_user()['first_name']+anvil.users.get_user()['last_name'][0]
  row = app_tables.prints.get(id=row['id'])
  app_tables.notes.add_row(print=row, notes=notes, user=user, date_time=date_string + '_' + time_string)

@anvil.server.callable
def get_notes(print_row):
  row = app_tables.prints.get(id=print_row['id'])
  note_row = app_tables.notes.search(print=row)
  return note_row

@anvil.server.callable
def delete_note(notes_row):
  user = anvil.users.get_user()['first_name']+anvil.users.get_user()['last_name'][0]
  user_role = anvil.users.get_user()['role']
  if notes_row['user'] == user:
    notes_row.delete()
  elif user_role == 'admin' or user_role == 'superadmin':
    notes_row.delete()
  else:
    raise Exception('You cannot delete other users\' notes.')
    
@anvil.server.callable
def get_wix_price(print_row):
  #product = app_tables.prints.get(id=id)
  inventory_row = app_tables.inventory.get(print=print_row)
  if not inventory_row:
    revenue = 0
    margin = 0
  else:
    revenue = float(inventory_row['price'][1:])-float(print_row['cost'])
    margin = float(revenue)/float(inventory_row['price'][1:])
    
  return inventory_row, revenue, "{:.2f}%".format(round(margin,2))
  
@anvil.server.callable
def calculate_revenue(print_row):
  inventory_row = get_wix_price(print_row)
  return float(inventory_row['price'][1:])-float(print_row['cost'])

@anvil.server.callable(require_user=authorization())
def link_stl_to_print(print_row, name):
  stl_row = app_tables.stls.get(name=name)
  stl_row.update(print=print_row)

@anvil.server.callable(require_user=authorization())
def delete_stl(filename):
  stl_row = app_tables.stls.get(name=filename)
  user_role = anvil.users.get_user()['role']
  if user_role == 'admin' or user_role == 'superadmin':
    stl_row.delete()
  else:
    raise Exception('You are not authorized to delete files.')

@anvil.server.callable(require_user=authorization())
def get_stl_data():
  return app_tables.stls.client_writable_cascade()