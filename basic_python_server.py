import 	socket
import threading





sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 20000))

sock.listen(1)

connections=[]


def handler(c, a):
	global connections
	while True:
		data=c.recv(1024)
		for connection in connections:
			connection.send(bytes(data))
		if not data:
			connections.remove(c)
			c.close()
			break





while True:
	c,a =sock.accept()
	cthread= threading.Thread( target= handler,args=(c,a))
	cthread.deamon=True
	cthread.start()
	connections.append(c)
	print(connections)




print("Hello World")