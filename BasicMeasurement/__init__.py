import time
import syslog
from sense_hat import SenseHat
import asyncio
sense = SenseHat()

class Module:
  def __init__(self, config):
    self.name = "BasicMeasurement"
    self.config = config
    self.seconds = 2

  def getSensorsData(self):
    return { "meta": { "timestamp":  time.time(), "client": self.config['client_id'], "module": self.config['module_id'] }, "data": { "humidity": sense.get_humidity(), "temp": sense.get_temperature(), "pressure": sense.get_pressure(), "acceler": sense.get_accelerometer()}}

  async def logData(self):
    while True:
      sense.set_pixel(0, 0, 239, 225, 99)
      syslog.syslog(str(self.getSensorsData())+"\n")
      await asyncio.sleep(self.seconds)
      sense.set_pixel(0, 0, 0, 0, 0)
      syslog.syslog(str(self.getSensorsData())+"\n")
      await asyncio.sleep(self.seconds)
  
  def startup(self):
    return self.logData