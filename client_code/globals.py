import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

selected_table = ''

def initial_install():
  if len(app_tables.services_status.search()) == 0:
    app_tables.services_status.add_row(job_status={}, printer_power_status={}, tenderslicer='Unknown', tendersystem='Unknown')
  if len(app_tables.settings.search()) == 0:
    app_tables.settings.add_row(outgoing_email_address='', selected_printer='')
  if len(app_tables.sync.search()) == 0:
    app_tables.sync.add_row(last_sync='never', id='products')