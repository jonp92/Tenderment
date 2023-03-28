import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_gcode_download(id):
  print_row = app_tables.prints.get_by_id(id)
  return anvil.BlobMedia(content_type="application/octet-stream", content=print_row['gcode'].get_bytes(), name=f"{print_row['name']}.gcode")

@anvil.server.callable()
def get_stl_download(print_row):
  stl_row = app_tables.stls.get(print=print_row)
  if not stl_row:
    raise Exception("No .stl file has been linked to this print")
  else:
   return anvil.BlobMedia(content_type="application/octet-stream", content=stl_row['stl'].get_bytes(), name=f"{stl_row['name']}")