import anvil.server
from anvil import *
import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media
from re import search, DOTALL, sub, MULTILINE, compile
from base64 import b64decode
from .Homepage import Homepage
from .Homepage import Upload
import datetime
import shortuuid
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
time_string =now.strftime("%H:%M:%S")
no_save = anvil.server.get_app_origin() + "/_/theme/no_save.png"

def sanitize_name(name):
  name_pattern = compile(r'^.*?(?=-\$)')
  name_match = name_pattern.search(name) 
  if name_match:
    name = name_match.group()
  else:
    name = filename
  return sub(r'%20', '_', name)

def find_print_info(name):
  match = search(r'\$(\d+\.\d+)-(\d{1,4}\.\d{1,4})g-(\d{1,2}.+).gcode', name)
  if match:
    cost = float(match.group(1))
    weight = float(match.group(2))
    time = match.group(3)
  else:
    cost = 0
    weight = 0
    time = 0
  return cost, weight, time

def upload_print_data(name, png, cost, weight, time, gcode):
  app_tables.prints.add_row(id=shortuuid.uuid(), name=name, media_object=png, uploaded=date_string, cost=round(cost,2), weight=round(weight,2), time=time, status='New', gcode=gcode)

@anvil.server.callable
def find_png(media_object, uploaded_file):
  name = sanitize_name(uploaded_file)
  cost, weight, time = find_print_info(uploaded_file)
  if name not in [r['name'] for r in app_tables.prints.search()]:
    with anvil.media.TempFile(media_object) as filename:
      with open(filename, 'r') as f:
        data = f.read()
      pattern = r'; thumbnail begin 500x500 \d{5,}(.+); thumbnail end'
      match = search(pattern, data, DOTALL)
      png_table = None
      if match:
          # logging.info('Thumbnail data found and copied, now to strip and decode using base64')
          thumbnail_data = match.group(1).strip()
          thumbnail_data = sub(r'^; ', '', thumbnail_data, flags=MULTILINE)
          thumbnail_data = b64decode(thumbnail_data)
          png = anvil.BlobMedia(content_type="image/png", content=thumbnail_data)
          upload_print_data(name=name, png=png, cost=cost, weight=weight, time=time, gcode=media_object)   
          return png, name
  else:
    return no_save, "File Already Exist"


    