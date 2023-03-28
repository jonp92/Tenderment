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
                 from_address = "support@tenderment.com",  
                 to = "jonathan@pressler.tech",
                 subject = "Test",
                 text = "This is a successful test of the Tenderment outbound email service.")
  
@anvil.email.handle_message(require_dkim=True)
def handle_incoming_emails(msg):
  msg.reply(text="Thank you for your message.")
  msg_row = app_tables.received_messages.add_row(
              from_addr=msg.envelope.from_address, 
              to=msg.envelope.recipient,
              text=msg.text, 
              html=msg.html
            )
  for a in msg.attachments:
    app_tables.attachments.add_row(
      message=msg_row, 
      attachment=a
    )