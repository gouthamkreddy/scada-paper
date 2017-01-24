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
### Start up the remote sync client
######################################################

client = ModbusClient('10.0.0.10', port=5023)
client.connect()

t = time.time()
while True:
    if time.time() - t >= 2.0:
        LA = client.read_holding_registers(REG_LA, 1).registers[0]
        L = client.read_holding_registers(REG_L, 1).registers[0]
        H = client.read_holding_registers(REG_H, 1).registers[0]
        HA = client.read_holding_registers(REG_HA, 1).registers[0]
        CURR = client.read_holding_registers(REG_CURR, 1).registers[0]
        MODE = client.read_coils(COIL_MODE, 1).bits[0]
        ON = client.read_coils(COIL_PUMP_MANUAL_ON_OFF, 1).bits[0]
        STATUS = client.read_coils(COIL_PUMP_STATUS, 1).bits[0]
        ALARM = client.read_coils(COIL_ALARM_STATUS, 1).bits[0]
        print "LA: ", LA
        print "L: ", L
        print "H: ", H
        print "HA: ", HA
        print "Current level: ", CURR
        print "Automatic Mode: ", MODE
        print "Manual Mode (On/Off): ", ON
        print "Pump Status (On/Off): ", STATUS
        print "Alarm Status (On/Off): ", ALARM
        t = time.time()
