from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

CURR = 64

client = ModbusClient('10.0.2.10', port=6060)
client.connect()

t = time.time()

while True:
    if time.time() - t >= 2.0:
        scanf
        client.write_register(CURR, 40)
        t = time.time()
