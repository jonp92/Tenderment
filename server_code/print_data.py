import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_prints(stat_search, status):
  if stat_search == 'Yes':
    return app_tables.prints.search(status=status)
  else:
    return app_tables.prints.search()

@anvil.server.callable
def get_print_by_id(id):
  return app_tables.prints.get_by_id(id)

@anvil.server.callable
def update_print_data(id, name, uploaded, time, cost, weight, status):
  update_row = app_tables.prints.get(id=id)
  update_row.update(name=name, uploaded=uploaded, time=float(time), cost=float(cost), weight=float(weight), status=status)

@anvil.server.callable
def get_gcode_download(id):
 print_row = app_tables.prints.get_by_id(id)
 return anvil.BlobMedia(content_type="application/octet-stream", content=print_row['gcode'].get_bytes(), name=f"{print_row['name']}.gcode")