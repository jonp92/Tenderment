import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import shortuuid

@anvil.server.callable
def upload_stl(file, filename):
  existing_row = app_tables.stls.get(name=filename)
  if not existing_row:
    app_tables.stls.add_row(name=filename, stl=file, id=shortuuid.uuid())
  else:
    raise Exception('Filename already exists, please rename the file before uploading')
@anvil.server.callable
def slice_stl_from_tables(stl_name):
  stl_row = app_tables.stls.get(name=stl_name)
  stl = stl_row['stl']
  anvil.server.call('main', stl, 'print_0.15mm', 'filament_PLA', '20%')