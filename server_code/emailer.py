import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def test_email_send():
  anvil.email.send(from_name = "Tenderment",
                 from_address = "no-reply@3dmk.xyz",  
                 to = "jonathan@pressler.tech",
                 subject = "Test",
                 text = "This is a successful test of the Tenderment outbound email service.")