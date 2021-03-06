import socket
addresses = []
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 44499))
serv.listen(5)
commandlist=['add', 'mul', 'div', 'sub']
help_r = '''
	
	Enter the command below to request in the Arithmetic server:
	>>add x y for [addition]
	>>sub x y for [subtraction]
	>>mul x y for [mutiplication]
	>>div x y for [division]
	>>quit or exit [to stop the process]

'''

while True:
    print "waiting for connection..."
    conn, addr = serv.accept()
    
    conn.send('Hello Welcome to Arithmetic Server.\n\n Enter "help" for help\n')
    if addr not in addresses:
        addresses.append(addr)
    print "connected at this address: "+ str(addr) 
    from_client = ''
    while True:
        data = conn.recv(4096)
        x = data.split()
        if data == "who is there" or x[0].lower() == "who":
            conn.send(str(addresses)+"\n".encode('utf-8'))
        elif data.lower() == "exit" or x[0].lower() == "exit" or data.lower() == "quit" or x[0].lower() == "quit":
            conn.send("bye~ ^^\n".encode('utf-8'))
            break
        elif data.lower() == "help" or x[0].lower() == "help":
            conn.send(help_r.encode('utf-8'))
        elif data == "geronyl" or x[0].lower() == "geronyl":
            conn.send("i love you Leah <3"+"\n".encode('utf-8'))
        elif not data:
            break
        elif x[0].lower() not in commandlist:
            conn.send("ERR: Wrong command inputed, ex. add, sub, mul, div.\n")
            break
        
        elif x[0].lower() == 'add':
            try:
                ans = int(x[1]) + int(x[2])
                print "client want to calculate: " + str(x[1]) + "+" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans)+"\n".encode('utf-8'))
            except:
    			conn.send("ERR: The value of x and y should be int.\n".encode('utf-8'))

        elif x[0].lower() == 'sub':
            try:
                ans = int(x[1]) - int(x[2])
                print "client want to calculate: " + str(x[1]) + "-" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans)+"\n".encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.\n".encode('utf-8'))

        elif x[0].lower() == 'mul':
            try:
                ans = int(x[1]) * int(x[2])
                print "client want to calculate: " + str(x[1]) + "*" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans)+"\n".encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.\n".encode('utf-8'))


        elif x[0].lower() == 'div':
            try:
                if x[1] == 0:
                    conn.send("ERR: Math Error.\n".encode('utf-8'))
                else:
                    ans = float(x[1]) / float(x[2])
                    print "client want to calculate: " + str(x[1]) + "/" + str(x[2])
                    print "Send: " + str(ans)
                    conn.send("The answer is: " + str(ans)+"\n".encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.\n".encode('utf-8'))
    
    conn.close()
    print 'client disconnected'
