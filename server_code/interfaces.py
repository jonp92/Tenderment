import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

#@anvil.server.background_task
#def update_services_status():
  #anvil.server.call('get_services_status')