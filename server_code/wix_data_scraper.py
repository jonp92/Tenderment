import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
import anvil.secrets
import json
import datetime
import pytz

product_url = f"stores/v1/products/query"
now = datetime.datetime.now(datetime.timezone.utc)
timezone_ny = pytz.timezone('America/New_York')
now_tz = now.astimezone(timezone_ny)
time_string_tz = now_tz.strftime("%H:%M:%S")
date_string = now.strftime("%Y_%m_%d")
time_string =now.strftime("%H:%M:%S")
User_Agent = 'Tenderment'
API_KEY = anvil.secrets.get_secret('wix')
wix_site_id = anvil.secrets.get_secret('wix-site-id')
API_URL = f"https://www.wixapis.com/"
headers = {'Authorization': f'{API_KEY}', 'User-Agent': f'{User_Agent}', 'Accept': "application/json, text/plain, */*", 'Content-Type': 'application/json', 'wix-site-id': f'{wix_site_id}'}


def authorization():
  if anvil.users.get_user():
    if anvil.users.get_user()['role'] == 'admin' or 'superadmin':
      return True
    else:
      return False
    
@anvil.server.callable    
def get_wix_products(url):
  url = f"{API_URL}{url}"
  response = anvil.http.request(url,
                                method="POST",
                                json=True, 
                                headers=headers,
                                data= {"includeVariants": 'true', 'query': {'paging': {'limit': "10"}}})                
  return response

@anvil.server.callable
def edit_sqqty(variantId, qty):
  pass


@anvil.server.callable(require_user=authorization())
def set_wix_products():
  sync_row = app_tables.sync.get(id='products')
  sync_row.update(last_sync=date_string + '-' + time_string_tz)
  url = f"{API_URL}{product_url}"
  response = anvil.http.request(url,
                                method="POST",
                                json=True, 
                                headers=headers,
                                data= {"includeVariants": 'true'})                
  for i in range(len(response['products'])):
    if app_tables.inventory.get(id=response['products'][i]['id']):
      row = app_tables.inventory.get(id=response['products'][i]['id'])
      row.update(name=response['products'][i]['name'], description=response['products'][i]['description'], price=response['products'][i]['price']['formatted']['price'], quantity=response['products'][i]['stock']['quantity'], last_sync=date_string + '-' + time_string)
    else:
      app_tables.inventory.add_row(name=response['products'][i]['name'], description=response['products'][i]['description'], price=response['products'][i]['price']['formatted']['price'], quantity=response['products'][i]['stock']['quantity'], id=response['products'][i]['id'], last_sync=date_string + '-' + time_string)

@anvil.server.callable
def get_wix_products_table():
  return app_tables.inventory.search()

@anvil.server.background_task
def sync_wix_data():
  set_wix_products()