import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def name_sanitizer(filename):
  import re
  first_pass = re.sub(r"[()\s_]+(?!\.)", "-", filename)
  second_pass = re.sub(r'\.stl$', '', first_pass)
  return re.sub(r"\)", "", second_pass)
  
@anvil.server.callable
def upload_stl(file, filename):
  import shortuuid
  filename = name_sanitizer(filename)
  existing_row = app_tables.stls.get(name=filename)
  if not existing_row:
    app_tables.stls.add_row(name=filename, stl=file, id=shortuuid.uuid())
    return filename
  else:
    raise Exception('Filename already exists, please rename the file before uploading')