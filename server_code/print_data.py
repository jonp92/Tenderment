import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import plotly.graph_objects as go

@anvil.server.callable
def count_prints():
  list = [r['id'] for r in app_tables.prints.search()]
  unique = count_unique(list)
  return pd.Series(unique).sum()

@anvil.server.callable
def prints_by_status():
  info = [
    {
      'name': r['name'],
      'status': r['status'],
   }
   for r in app_tables.prints.search()
  ]
  df = pd.DataFrame(info, columns=['name', 'status'])
  df = df.groupby('status').count().reset_index()
  return go.Bar(x=df['status'], y=df['name'], text="Prints In"+df['status'])

@anvil.server.callable
def count_unique(list):
  return pd.Series(list).value_counts()

@anvil.server.callable
def get_prints(stat_search, status):
  if stat_search == 'Yes':
    return app_tables.prints.search(status=status)
  else:
    return app_tables.prints.search()

@anvil.server.callable
def get_print_by_id(id):
  return app_tables.prints.get_by_id(id)

@anvil.server.callable
def update_print_data(id, name, uploaded, time, cost, weight, status):
  update_row = app_tables.prints.get(id=id)
  update_row.update(name=name, uploaded=uploaded, time=time, cost=float(cost), weight=float(weight), status=status)

@anvil.server.callable
def get_gcode_download(id):
 print_row = app_tables.prints.get_by_id(id)
 return anvil.BlobMedia(content_type="application/octet-stream", content=print_row['gcode'].get_bytes(), name=f"{print_row['name']}.gcode")

@anvil.server.callable
def delete_row(row):
  row.delete()

@anvil.server.callable
def add_note(row, notes):
  row = app_tables.prints.get(id=row['id'])
  app_tables.notes.add_row(print=row, notes=notes)
  