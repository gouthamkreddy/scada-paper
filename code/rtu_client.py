from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

REG_LA = 0
REG_L = 16
REG_H = 32
REG_HA = 48
REG_CURR = 64
COIL_MODE = 80
COIL_PUMP_MANUAL_ON_OFF = 81
COIL_PUMP_STATUS = 82
COIL_ALARM_STATUS = 83

######################################################
### Start up the sync client
######################################################

client = ModbusClient('localhost', port=5023)
client.connect()

# If Mode is True then automatic
client.write_coil(COIL_MODE, True)

client.write_coil(COIL_PUMP_MANUAL_ON_OFF, True)

client.write_coil(COIL_PUMP_STATUS, True)

client.write_coil(COIL_ALARM_STATUS, False)

client.write_register(REG_LA, 20)
client.write_register(REG_HA, 120)
client.write_register(REG_L, 40)
client.write_register(REG_H, 100)
client.write_register(REG_CURR, 40)

t = time.time()

while True:
    mode = client.read_coils(COIL_MODE, 1).bits[0]
    on = client.read_coils(COIL_PUMP_MANUAL_ON_OFF, 1).bits[0]
    curr = client.read_holding_registers(REG_CURR, 1).registers[0]
    if mode == True:
        if on == True:
            if curr < 100:
                while time.time() - t < 0.1:
                    continue
                t = time.time()
                client.write_register(REG_CURR, curr+1)
            else:
                client.write_coil(COIL_PUMP_STATUS, False)
        else:
            if curr > 40:
                while time.time() - t < 0.1:
                    continue
                t = time.time()
                client.write_register(REG_CURR, curr-1)
            else:
                client.write_coil(COIL_PUMP_STATUS, True)
    print curr
    if (curr == 20) || (curr == 120):
        client.write_coil(COIL_ALARM_STATUS, True)
