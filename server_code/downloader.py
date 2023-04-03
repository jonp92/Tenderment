import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def authorization():
  if anvil.users.get_user():
    if anvil.users.get_user()['role'] == 'admin' or 'superadmin':
      return True
    else:
      return False

@anvil.server.callable(require_user=authorization())
def get_gcode_download(id):
  print_row = app_tables.prints.get_by_id(id)
  if not stl_row:
    raise Exception("Unable to locate print.")
  else:  
    return anvil.BlobMedia(content_type="application/octet-stream", content=print_row['gcode'].get_bytes(), name=f"{print_row['name']}.gcode")

@anvil.server.callable(require_user=authorization())
def get_stl_download(print_row):
  stl_row = app_tables.stls.get(print=print_row)
  if not stl_row:
    raise Exception("No .stl file has been linked to this print")
  else:
   return anvil.BlobMedia(content_type="application/octet-stream", content=stl_row['stl'].get_bytes(), name=f"{stl_row['name']}")

@anvil.server.callable(require_user=authorization())
def get_email_attachments(email_row):
  attachments_row = app_tables.attachments.get(message=email_row)
  if not attachments_row:
    raise Exception("Unable to locate any attachments.")
  else:
    if not attachments_row['filename']:
      attachments_row['filename'] = 'none'
    return anvil.BlobMedia(content_type="application/octet-stream", content=attachments_row['attachment'].get_bytes(), name=attachments_row['filename'])
  