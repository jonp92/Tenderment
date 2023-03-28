import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def update_settings(settingsdict):
  row = app_tables.settings.get()
  row.update(selected_printer=settingsdict['selected_printer'])

@anvil.server.callable
def get_settings():
  return [r['selected_printer'] for r in app_tables.settings.search()][0]