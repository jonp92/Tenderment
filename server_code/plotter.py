import anvil.email
#import anvil.users
import anvil.server

@anvil.server.callable
def plot_prints_by_status():
  from anvil.tables import app_tables
  import plotly.graph_objects as go
  import pandas as pd
  info = [
    {
      'name': r['name'],
      'status': r['status'],
   }
   for r in app_tables.prints.search()
  ]
  df = pd.DataFrame(info, columns=['name', 'status'])
  df = df.groupby('status').count().reset_index()
  return go.Bar(x=df['status'], y=df['name'], text=df['status'])

@anvil.server.callable
def plot_prints_pie():
  from anvil.tables import app_tables
  import plotly.graph_objects as go
  import pandas as pd
  info = [
    {
      'name': r['name'],
      'status': r['status'],
   }
   for r in app_tables.prints.search()
  ]
  list = [r['id'] for r in app_tables.prints.search()]
  df = pd.DataFrame(info, columns=['name', 'status'])
  df = df.groupby('status').count().reset_index()
  return go.Pie(labels=df['status'], values=df['name']), pd.Series(pd.Series(list).value_counts()).sum()

@anvil.server.callable
def plot_stl(fileName):
  from anvil.tables import app_tables
  import anvil.mpl_util
  import numpy as np
  import pandas as pd
  from stl import mesh
  import matplotlib.pyplot as plt
  # Create a new plot
  figure = plt.figure()
  axes = mplot3d.Axes3D(figure)

  # Load the STL files and add the vectors to the plot
  stl_row = app_tables.stls.get(name=fileName)
  stl = stl_row['stl']
  with anvil.media.TempFile(stl) as stl_file:
    your_mesh = mesh.Mesh.from_file(stl_file)
  axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

  # Auto scale to the mesh size
  scale = your_mesh.points.flatten()
  axes.auto_scale_xyz(scale, scale, scale)

  # Show the plot to the screen
  return anvil.mpl_util.plot_image()