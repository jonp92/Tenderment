import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def update_settings(filter, item):
  row = (app_tables.settings.get()
            or app_tables.settings.add_row(outgoing_email_address=item['outgoing_email_address'], selected_printer=item['selected_printer']))
  if filter == 1:
    row.update(selected_printer=item['selected_printer'])
  elif filter == 2:
    row.update(outgoing_email_address=item['outgoing_email_address'])

@anvil.server.callable
def get_settings():
  return [r['selected_printer'] for r in app_tables.settings.search()][0]