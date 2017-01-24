from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

######################################################
### Start up the async server
######################################################

store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [0]*100)
)
context = ModbusServerContext(slaves=store, single=True)


identity = ModbusDeviceIdentification()

StartTcpServer(context, identity=identity, address=("localhost", 5023))
