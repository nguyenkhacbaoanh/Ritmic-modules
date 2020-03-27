#!/usr/bin/python3

# ----------- Ritmic -----------
# Author: Wladimir Delenclos
# Licence: MIT
# ------------------------------

from sense_hat import SenseHat
import time
import json
import uuid
import importlib
import imp
import asyncio


sense = SenseHat()
loop = asyncio.get_event_loop()

class Main:
  # Init Class
  def __init__(self):
    with open("./config.json", 'r') as f:
      data = json.loads(f.read()) #data becomes a dictionary
      data['module_id'] = hex(uuid.getnode())
    #and then just write the data back on the file
    with open("./config.json", 'w') as f:
      f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    with open('./config.json') as json_file:
      data = json.load(json_file)
      self.config = data
  # Init modules
  def init(self):
    sense.load_image('./_src/assets/logo_blue.png')
    print("\n\n----------- Starting Rtimic module -----------\n|\n|  Client : " + self.config['client_id']+ "\n|  Module id : " + self.config['module_id'] + "\n|\n----------------------------------------------")
    print('Modules loaded :')
    for module in self.config["modules_enabled"]:
      module = imp.load_source( 'file1', './'+ module + '/__init__.py')
      Module = module.Module(self.config)
      starter = Module.startup()
      asyncio.ensure_future(starter())
    try:
      loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("SERVICE STOPPED")
        loop.close()

Ritmic = Main()
Ritmic.init()