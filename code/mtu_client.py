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

client = ModbusClient('10.0.2.10', port=6060)
client.connect()

t = time.time()

while True:
    if time.time() - t >= 2.0:
        LA1 = client.read_holding_registers(LA, 1).registers[0]
        L1 = client.read_holding_registers(L, 1).registers[0]
        H1 = client.read_holding_registers(H, 1).registers[0]
        HA1 = client.read_holding_registers(HA, 1).registers[0]
        CURR1 = client.read_holding_registers(CURR, 1).registers[0]
        MODE1 = client.read_coils(MODE, 1).bits[0]
        ON1 = client.read_coils(PUMP_MANUAL, 1).bits[0]
        STATUS1 = client.read_coils(PUMP_STATUS, 1).bits[0]
        ALARM1 = client.read_coils(ALARM_STATUS, 1).bits[0]
        print "LA: ", LA1
        print "L: ", L1
        print "H: ", H1
        print "HA: ", HA1
        print "Current level: ", CURR1
        print "Automatic Mode: ", MODE1
        print "Manual Mode (On/Off): ", ON1
        print "Pump Status (On/Off): ", STATUS1
        print "Alarm Status (On/Off): ", ALARM1
        t = time.time()
