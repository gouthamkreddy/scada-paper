#!/usr/bin/python -i

# Extra Assignment CS425
# Arunothia Marappan (13378)

# Create a WAN 

from core import pycore

session = pycore.Session(persistent=True)
n1 = session.addobj(cls = pycore.nodes.class, name="n1")
n1.setposition(x=53.0,y=588.0)
n2 = session.addobj(cls = pycore.nodes.class, name="n2")
n2.setposition(x=287.0,y=582.0)
n3 = session.addobj(cls = pycore.nodes.class, name="n3")
n3.setposition(x=388.0,y=518.0)
e1 = session.addobj(cls = pycore.nodes.class, name="e1")
e1.setposition(x=187.0,y=348.0)
e2 = session.addobj(cls = pycore.nodes.class, name="e2")
e2.setposition(x=624.0,y=219.0)
n5 = session.addobj(cls = pycore.nodes.class, name="n5")
n5.setposition(x=556.0,y=380.0)
n6 = session.addobj(cls = pycore.nodes.class, name="n6")
n6.setposition(x=781.0,y=364.0)
n7 = session.addobj(cls = pycore.nodes.class, name="n7")
n7.setposition(x=824.0,y=272.0)
n8 = session.addobj(cls = pycore.nodes.class, name="n8")
n8.setposition(x=848.0,y=146.0)
n4 = session.addobj(cls = pycore.nodes.class, name="n4")
n4.setposition(x=375.0,y=301.0)
r1 = session.addobj(cls = pycore.nodes.class, name="r1")
r1.setposition(x=443.0,y=78.0)
n1.newnetif(net=e1, addrlist=["10.0.1.20/24"], ifindex=1)
n2.newnetif(net=e1, addrlist=["10.0.1.21/24"], ifindex=1)
n3.newnetif(net=e1, addrlist=["10.0.1.22/24"], ifindex=0)
r1.newnetif(net=e1, addrlist=["10.0.1.1/24"], ifindex=0)
n5.newnetif(net=e2, addrlist=["10.0.2.20/24"], ifindex=0)
n6.newnetif(net=e2, addrlist=["10.0.2.21/24"], ifindex=0)
n7.newnetif(net=e2, addrlist=["10.0.2.22/24"], ifindex=0)
n8.newnetif(net=e2, addrlist=["10.0.2.23/24"], ifindex=0)
n4.newnetif(net=e2, addrlist=["10.0.2.24/24"], ifindex=0)
r1.newnetif(net=e2, addrlist=["10.0.2.1/24"], ifindex=1)
n1.newnetif(net=ptpnet, addrlist=["10.0.0.20/24"], ifindex=0)
n2.newnetif(net=ptpnet, addrlist=["10.0.0.21/24"], ifindex=0)
session.shutdown()

if __name__ == "__main__" or __name__ == "__builtin__":
    main()

def add_to_server(session):
    ''' Add this session to the server's list if this script is executed from
    the core-daemon server.
    '''
    global server
    try:
        server.addsession(session)
        return True
    except NameError:
        return False
	

