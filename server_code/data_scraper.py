import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.secrets

class sqspace:
  User_Agent = 'Tenderment'
  API_KEY = anvil.secrets.get_secret('sqspace')
  API_URL = f"https://api.squarespace.com/"
  API_VER = f"1.0"
  def _init_(self, API_URL, API_VER):
    self.API_URL = API_URL
    self.API_VER = API_VER
     
  @anvil.server.callable
  def get_inventory(self):
    INV_URL = self.API_URL+self.API_VER+f"commerce/inventory"
    print(INV_URL)
    response = anvil.http.request(INV_URL, method="GET", json=True, headers={'Authorization': f'Bearer {self.API_KEY}', 'User-Agent': f'{self.User_Agent}'})
    return response

print(sqspace().get_inventory())