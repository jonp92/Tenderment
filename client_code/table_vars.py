import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

selected_table = ''

def check_if_settings_exists():
  if len(app_tables.settings.search()) == 0:
    app_tables.settings.add_row(outgoing_email_address='', selected_printer='')