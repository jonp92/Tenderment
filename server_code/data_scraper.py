import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.secrets

class sqspace:
  def _init_(self):
    self.User_Agent = 'Tenderment'
    self.API_KEY = anvil.secrets.get_secret('sqspace')

  @anvil.server.callable
  def get_inventory(self):
    self.API_URL = f"https://api.squarespace.com/1.0/commerce/inventory"
    self.response = anvil.http.request(self.API_URL, method="GET", json=True, headers={'Authorization': f'Bearer {self.API_KEY}', 'User-Agent': f'{self.User_Agent}'})
    self.API_KEY
    return self.response

print(sqspace().get_inventory())