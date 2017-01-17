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
COIL_PUMP_STATUS = 82
COIL_ALARM_STATUS = 83

######################################################
### Start up the sync client
######################################################

client = ModbusClient('10.0.2.11', port=5023)
client.connect()



while True:
	lines = tuple(open('file.txt', 'r'))
	a = lines[0].split(',');
	La = int(a[0])
	L = int(a[1])
	H = int(a[2])
	Ha = int(a[3])
	mode = int(a[4])
	pump = int(a[5])
	#curr = int(a[6])
	client.write_register(REG_LA, La)
	client.write_register(REG_HA, Ha)
	client.write_register(REG_L, L)
	client.write_register(REG_H, H)
	c = client.read_holding_registers(REG_CURR, 1).registers[0]
	
	if mode == 1:
		client.write_coil(COIL_MODE, True)
	else:
		client.write_coil(COIL_MODE, False)
		if pump == 1:
			client.write_coil(COIL_PUMP_STATUS, True)
		else:
			client.write_coil(COIL_PUMP_STATUS, False)
	with open("status.txt", "w") as text_file:
		text_file.write("%s" % str(c))
