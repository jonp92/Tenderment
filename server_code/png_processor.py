import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media
from re import search, DOTALL, sub, MULTILINE
from base64 import b64decode
from .MainForm import MainForm
import datetime
now = datetime.datetime.now()
date_string = now.strftime("%m_%d_%Y-%H:%M:%S")
@anvil.server.callable
def find_png(media_object, uploaded_file):
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
        return_media = anvil.BlobMedia(content_type="image/png", content=thumbnail_data)
        if uploaded_file not in [r['name'] for r in app_tables.images.search()]:
          png_table = app_tables.images.add_row(name=uploaded_file, media_object=return_media, uploaded=date_string)
    return return_media

@anvil.server.callable
def find_png_gcode(data, filename):
    pattern = r'; thumbnail begin 500x500 \d{5,}(.+); thumbnail end'
    match = search(pattern, data, DOTALL)
    new_row = None
    if match:
        # logging.info('Thumbnail data found and copied, now to strip and decode using base64')
        thumbnail_data = match.group(1).strip()
        thumbnail_data = sub(r'^; ', '', thumbnail_data, flags=MULTILINE)
        thumbnail_data = b64decode(thumbnail_data)
        return_media_gcode = anvil.BlobMedia(content_type="image/png", content=thumbnail_data)
        if filename not in [r['name'] for r in app_tables.images.search()]:
          new_row = app_tables.images.add_row(name=filename, media_object=return_media_gcode, uploaded=date_string)
    return return_media_gcode
    