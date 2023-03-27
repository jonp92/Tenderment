#import anvil.secrets
#import anvil.users
#import anvil.tables as tables
#import anvil.tables.query as q
#from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def set_form_session(open_form):
 anvil.server.session['open_form'] = open_form

@anvil.server.callable
def get_form_session():
  return anvil.server.session.get('open_form')