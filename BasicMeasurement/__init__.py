import time
import logging
import asyncio
import os
from logging.handlers import RotatingFileHandler
from sense_hat import SenseHat

sense = SenseHat()


class Module:
  def __init__(self, config):
    self.name = "BasicMeasurement"
    self.config = config

  def getSensorsData(self):
    return { "meta": { "timestamp":  time.time(), "client": self.config['client_id'], "module": self.config['module_id'] }, "data": { "humidity": sense.get_humidity(), "temp": sense.get_temperature(), "pressure": sense.get_pressure(), "acceler": sense.get_accelerometer()}}

  async def logData(self):
    logFile = self.config['log_directory'] +'/'+ self.name + '.log'
    try:
      os.mkdir(self.config['log_directory'])
      print("✔️ Directory " , self.config['log_directory'] ,  " Created ") 
    except FileExistsError:
      print("✔️ Directory " , self.config['log_directory'] ,  " already exists")
    try:
      file = open(logFile, 'r')
      print("✔️ Log file " , logFile ,  " Created ") 
    except IOError:
      file = open(logFile, 'w')
      print("✔️ Log file " , logFile ,  " already exists ") 
    logging.basicConfig(filename=logFile,level=logging.INFO)
    print('✔️ Module is running')

    while True:
      sense.set_pixel(0, 0, 239, 225, 99)
      logging.info(str(self.getSensorsData()))
      await asyncio.sleep(self.config['frequency'])
      sense.set_pixel(0, 0, 0, 0, 0)
      logging.info(str(self.getSensorsData()))
      await asyncio.sleep(self.config['frequency'])

  def startup(self):
    return self.logData