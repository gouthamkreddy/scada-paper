from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from random import randint
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
COIL_PUMP_STATUS = 82
COIL_ALARM_STATUS = 83

######################################################
### Start up the sync client
######################################################

client = ModbusClient('10.0.2.11', port=5023)
client.connect()

# If Mode is True then automatic
client.write_coil(COIL_MODE, True)

client.write_coil(COIL_PUMP_STATUS, True)

client.write_coil(COIL_ALARM_STATUS, False)

client.write_register(REG_LA, 20)
client.write_register(REG_HA, 120)
client.write_register(REG_L, 40)
client.write_register(REG_H, 100)
client.write_register(REG_CURR, 40)

t = time.time()

while True:
	La = client.read_holding_registers(REG_LA, 1).registers[0]
	L = client.read_holding_registers(REG_L, 1).registers[0]
	H = client.read_holding_registers(REG_H, 1).registers[0]
	Ha = client.read_holding_registers(REG_HA, 1).registers[0]
	c = client.read_holding_registers(REG_CURR, 1).registers[0]
	print ("Current water level - %d") % (c)
	print ("%d %d %d %d") %(La,L,H,Ha)
	mode = client.read_coils(COIL_MODE, 1).bits[0]
	on = client.read_coils(COIL_PUMP_STATUS, 1).bits[0]
	curr = client.read_holding_registers(REG_CURR, 1).registers[0]
	if mode == False:
		if on == True:
			while time.time() - t < 0.1:
				continue
			t = time.time()
			if curr<120:
				client.write_register(REG_CURR, curr+1)
		else:
			while time.time() - t < 0.1:
				continue
			t = time.time()
			if curr>0:
				client.write_register(REG_CURR, curr-1)
				
	if mode == True:
		if on == True:
			if curr < H:
				while time.time() - t < 0.1:
					continue
				t = time.time()
				client.write_register(REG_CURR, curr+1)
			else:
				client.write_coil(COIL_PUMP_STATUS, False)
		else:
			if curr > L:
				while time.time() - t < 0.1:
					continue
				t = time.time()
				client.write_register(REG_CURR, curr-1)
			else:
				client.write_coil(COIL_PUMP_STATUS, True)
	if (curr <= La) or (curr >= Ha):
		client.write_coil(COIL_ALARM_STATUS, True)
		curr = randint(1,120)
		client.write_coil(COIL_ALARM_STATUS, False)
	
