import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.background_task
def get_printer_status():
  printer_power_status = anvil.server.call('get_printer_power_status')
  status_row = app_tables.services_status.get()
  status_row.update(printer_power_status=printer_power_status)