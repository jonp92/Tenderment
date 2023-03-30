import anvil.email
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

def authorization():
  if anvil.users.get_user():
    if anvil.users.get_user()['role'] == 'admin' or 'superadmin':
      return True
    else:
      return False

@anvil.server.callable
def test_email_send(to):
  anvil.email.send(from_name = "Tenderment",
                 from_address = "support@tenderment.com",  
                 to = to,
                 subject = "Test",
                 text = "This is a successful test of the Tenderment outbound email service.")
  
@anvil.email.handle_message(require_dkim=True)
def handle_incoming_emails(msg):
  msg.reply(text="Thank you for your message.")
  msg_row = app_tables.received_messages.add_row(
              from_addr=msg.envelope.from_address, 
              to=msg.envelope.recipient,
              subject=msg.subject,
              text=msg.text, 
              html=msg.html
            )
  for a in msg.attachments:
    app_tables.attachments.add_row(message=msg_row, attachment=a)
  for header, a in msg.inline_attachments.items():
    app_tables.attachments.add_row(
      message=msg_row,
      attachment=a
    )  
    
@anvil.server.callable(require_user=authorization())
def get_email_data():
  return app_tables.received_messages.client_writable_cascade()

@anvil.server.callable(require_user=authorization())
def get_attachments(msg_row):
  attachments = app_tables.attachments.get(message=msg_row)
  if attachments:
    return attachments['attachment']