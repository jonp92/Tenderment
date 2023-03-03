import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.secrets

User_Agent = 'Tenderment'
API_KEY = anvil.secrets.get_secret('sqspace')
API_URL = f"https://api.squarespace.com/"
API_VER = f"1.0"

@anvil.server.callable
def get_inventory():
  INV_URL = API_URL+API_VER+f"/commerce/inventory"
  response = anvil.http.request(INV_URL, method="GET", json=True, headers={'Authorization': f'Bearer {API_KEY}', 'User-Agent': f'{User_Agent}'})
  return response
  
def get_orders():
  ORD_URL = API_URL+API_VER+f"/commerce/orders"
  response = anvil.http.request(ORD_URL, method="GET", json=True, headers={'Authorization': f'Bearer {API_KEY}', 'User-Agent': f'{User_Agent}'})
  return response