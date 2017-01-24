from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

LA = 0
L = 16
H = 32
HA = 48
CURR = 64
MODE = 80
PUMP_MANUAL = 81
PUMP_STATUS = 82
ALARM_STATUS = 83

client = ModbusClient('localhost', port=6060)
client.connect()

# If Mode is True then automatic
client.write_coil(MODE, True)
client.write_coil(PUMP_MANUAL, True)
client.write_coil(PUMP_STATUS, True)
client.write_coil(ALARM_STATUS, False)

client.write_register(LA, 20)20
client.write_register(HA, 80)120
client.write_register(L, 30)40
client.write_register(H, 70)100
client.write_register(CURR, 40)

t = time.time()

while True:
    mode = client.read_coils(MODE, 1).bits[0]
    on = client.read_coils(PUMP_MANUAL, 1).bits[0]
    curr = client.read_holding_registers(CURR, 1).registers[0]
    if mode == True:
        if on == True:
            if curr < 70:
                while time.time() - t < 0.1:
                    continue
                t = time.time()
                client.write_register(CURR, curr+1)
            else:
                client.write_coil(PUMP_STATUS, False)
        else:
            if curr > 30:
                while time.time() - t < 0.1:
                    continue
                t = time.time()
                client.write_register(CURR, curr-1)
            else:
                client.write_coil(PUMP_STATUS, True)
    print curr
    if (curr <= 20) || (curr >= 80):
        client.write_coil(COIL_ALARM_STATUS, True)
