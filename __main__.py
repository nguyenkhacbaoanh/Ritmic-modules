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

# Set path of the script
path = "/home/ritmic/Ritmic-modules/"

sense = SenseHat()
loop = asyncio.get_event_loop()
configFile = path +'config.json'
class Main:
  # Init Class
  def __init__(self):
    with open(configFile, 'r') as f:
      data = json.loads(f.read()) #data becomes a dictionary
      data['module_id'] = hex(uuid.getnode())
    #and then just write the data back on the file
    with open(configFile, 'w') as f:
      f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    with open(configFile) as json_file:
      data = json.load(json_file)
      self.config = data
  # Init modules
  def init(self):
    sense.load_image(path+'_src/assets/logo_blue.png')
    print("\n\n----------- Starting Rtimic module -----------\n|\n|  Client : " + self.config['client_id']+ "\n|  Module id : " + self.config['module_id'] + "\n|\n----------------------------------------------")
    print('⚙️ Initialisation')
    for module in self.config["modules_enabled"]:
      module = imp.load_source( 'file1', path + module + '/__init__.py')
      Module = module.Module(self.config)
      starter = Module.startup()
      asyncio.ensure_future(starter())
    try:
      loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("✖️ Modules Stopped")
        sense.clear()
        loop.close()

Ritmic = Main()
Ritmic.init()