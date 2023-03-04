import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_print_by_id(id):
  return app_tables.prints.get_by_id(id)

@anvil.server.callable
def update_print_data(print_data):
  update_row = app_tables.prints.add_row(id=print_data['id'])
  print(update_row)