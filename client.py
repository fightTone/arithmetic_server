import socket
print('''
	Hello This is the an arithmetic client file.
	Enter the command below to request in the Arithmetic server:
	>>add x y for [addition]
	>>sub x y for [subtraction]
	>>mul x y for [mutiplication]
	>>div x y for [division]
	>>geronyl [special command]
	>>quit or exit [to stop the process]

''')


while True:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('210.213.231.10', 14399))
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