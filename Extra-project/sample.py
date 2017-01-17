from core import pycore
def main():
	session = pycore.Session(persistent=True)
	node1 = session.addobj(cls=pycore.nodes.CoreNode, name="n1")
	node2 = session.addobj(cls=pycore.nodes.CoreNode, name="n2")
	hub1 = session.addobj(cls=pycore.nodes.HubNode, name="hub1")
	node1.newnetif(hub1, ["10.0.0.1/24"])
	node2.newnetif(hub1, ["10.0.0.2/24"])

	node1.icmd(["ping", "-c", "5", "10.0.0.2"])
	session.shutdown()



if __name__ == "__main__" or __name__ == "__builtin__":
    main()