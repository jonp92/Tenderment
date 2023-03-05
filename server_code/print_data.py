import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_prints():
  return app_tables.prints.search()

@anvil.server.callable
def get_print_by_id(id):
  return app_tables.prints.get_by_id(id)

@anvil.server.callable
def update_print_data(id, name, uploaded, time, cost, weight, status):
  update_row = app_tables.prints.get(id=id)
  #name = print_data['name']
  #uploaded = print_data['uploaded']
  #time = print_data['time']
  #cost = print_data['cost']
  #weight = print_data['weight']
  #status = print_data['status'] 
  update_row.update(name=name, uploaded=uploaded, time=float(time), cost=float(cost), weight=float(weight), status=status)