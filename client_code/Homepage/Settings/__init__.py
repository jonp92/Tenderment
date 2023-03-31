from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..TableExplorer import TableExplorer
from .LogTail import LogTail
from .TestEmail import TestEmail

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.

    self.init_components(**properties)
    self.drop_down_printer.items = [r['printers'] for r in app_tables.printers.search()]
    self.item['selected_printer'] = [r['selected_printer'] for r in app_tables.settings.search()][0]
    self.drop_down_printer.selected_value = self.item['selected_printer']
    self.item['outgoing_email_address'] = [r['outgoing_email_address'] for r in app_tables.settings.search()][0]
    self.text_box_outgoing_email_address.text = self.item['outgoing_email_address']
    self.button_expand_email_options.tag = 'down'
    
    # Any code you write here will run before the form opens.

  def button_table_explorer_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('set_form_session', 'TableExplorer')
    form = get_open_form()
    form.column_panel_2.clear()
    form.column_panel_2.add_component(TableExplorer(), full_width_row=True)

  def button_test_email_click(self, **event_args):
    """This method is called when the button is clicked"""
    send_test_email = alert(TestEmail(item=self.item), title='Enter an email address to send a test message.', large=True)
    if send_test_email:
      with Notification('A test email was sent to ' + self.item['test_email_address'], style='success', title='Email Sent!'):
        anvil.server.call('test_email_send', self.item['test_email_address'])

  def button_restart_server_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('reset_server')
    Notification('The Tenderment Anvil Service has been restarted on delta.badjholdings.com', style='success').show()

  def button_git_pull_click(self, **event_args):
    """This method is called when the button is clicked"""
    git_result = anvil.server.call('git_latest_config')
    Notification(git_result).show()

  def button_tail_anvil_log_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(LogTail(self.text_box_lines_tail.text, self.drop_down_log_selected.selected_value), title=f'Tail of {self.drop_down_log_selected.selected_value} Log', large=True)

  def button_save_email_options_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_settings', 2, self.item)
    self.refresh_data_bindings()

  def button_slicing_options_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_settings', 1, self.item)

  def button_expand_email_options_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.button_expand_email_options.tag == 'down':
      self.button_expand_email_options.icon = 'fa:angle-up'
      self.button_expand_email_options.tag = 'up'
      self.grid_panel_emaiL_options.visible = True
    elif self.button_expand_email_options.tag == 'up':
      self.button_expand_email_options.icon = 'fa:angle-down'
      self.button_expand_email_options.tag = 'down'
      self.grid_panel_emaiL_options.visible = False     











    


