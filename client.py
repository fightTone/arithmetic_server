import socket
i=0
while i==0:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('210.213.231.10', 44499))
	from_server = client.recv(4096)
	print (from_server.decode('utf-8'))
	while True:
		
		npt = raw_input("enter command: ")
		client.send(npt.encode('utf-8'))
		from_server = client.recv(4096)
		if npt ==  'geronyl':
			while True:
				print (from_server.decode('utf-8'))
		else:
			print (from_server.decode('utf-8'))
		if npt.lower() == "quit" or npt.lower() == "exit":
			break
	
	client.close()
	i+=1
