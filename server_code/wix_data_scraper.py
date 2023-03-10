import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.secrets
import json
import uuid

User_Agent = 'Tenderment v0.8.2'
API_KEY = anvil.secrets.get_secret('wix')
wix_site_id = anvil.secrets.get_secret('wix-site-id')
API_URL = f"https://www.wixapis.com/"
headers = {'Authorization': f'{API_KEY}', 'User-Agent': f'{User_Agent}', 'Accept': "application/json, text/plain, */*", 'Content-Type': 'application/json', 'wix-site-id': f'{wix_site_id}'}
@anvil.server.callable
def get_wix_products(url):
  url = f"{API_URL}{url}"
  response = anvil.http.request(url,
                                method="POST",
                                json=True, 
                                headers=headers,
                                data= {}
                              )                
  return response

@anvil.server.callable
def edit_sqqty(variantId, qty):
  pass
