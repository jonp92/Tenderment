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

User_Agent = 'Tenderment v0.5'
API_KEY = anvil.secrets.get_secret('sqspace')
API_URL = f"https://api.squarespace.com/"
API_VER = f"1.0"
SQ_URL = API_URL+API_VER
uuidsq = uuid.uuid4()
headers = {'Authorization': f'Bearer {API_KEY}', 'User-Agent': f'{User_Agent}', 'Idempotency-Key': f'{uuidsq}', 'Content-Type': 'application/json'}
@anvil.server.callable
def get_sqdata(url):
  SQ_URL_COMPLETE = SQ_URL+url
  response = anvil.http.request(SQ_URL_COMPLETE,
                                method="GET",
                                json=True, 
                                headers={'Authorization': f'Bearer {API_KEY}', 'User-Agent': f'{User_Agent}'})
  return response

@anvil.server.callable
def edit_sqqty(variantId, qty):
  SQ_URL_COMPLETE = SQ_URL+f"/commerce/inventory/adjustments"
  print(headers)
  print({
	"setFiniteOperations": [{
		"variantId": f"{variantId}",
		"quantity": qty
	}]
})
  anvil.http.request(SQ_URL_COMPLETE,
                     method="POST",
                     json=True,
                     headers=headers,
                     data=
'{
	"setFiniteOperations": [{
		"variantId": f"{variantId}",
		"quantity": qty
	}]
}'
)

