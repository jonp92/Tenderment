import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media


@anvil.server.callable
def plot_prints_by_status():
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
  return go.Pie(labels=df['status'], values=df['name'])

@anvil.server.callable
def plot_stl(fileName):
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