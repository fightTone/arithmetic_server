import socket
addresses = []
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 80))
serv.listen(5)
commandlist=['add', 'mul', 'div', 'sub']
while True:
    print "waiting for connection..."
    conn, addr = serv.accept()
    if addr not in addresses:
        addresses.append(addr)
    print "connected at this address: "+ str(addr) 
    from_client = ''
    while True:
        data = conn.recv(4096)
        x = data.split()
        if data == "who is there":
            conn.send(str(addresses).encode('utf-8'))
        elif data == "geronyl":
            conn.send("i love you Leah <3".encode('utf-8'))
        elif not data:
            break
        elif x[0].lower() not in commandlist:
            conn.send("ERR: Wrong command inputed, ex. add, sub, mul, div.")
            break
        
        elif x[0].lower() == 'add':
            try:
                ans = int(x[1]) + int(x[2])
                print "client want to calculate: " + str(x[1]) + "+" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans).encode('utf-8'))
            except:
    			conn.send("ERR: The value of x and y should be int.".encode('utf-8'))

        elif x[0].lower() == 'sub':
            try:
                ans = int(x[1]) - int(x[2])
                print "client want to calculate: " + str(x[1]) + "-" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans).encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.".encode('utf-8'))

        elif x[0].lower() == 'mul':
            try:
                ans = int(x[1]) * int(x[2])
                print "client want to calculate: " + str(x[1]) + "*" + str(x[2])
                print "Send: " + str(ans)
                conn.send("The answer is: " + str(ans).encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.".encode('utf-8'))


        elif x[0].lower() == 'div':
            try:
                if x[1] == 0:
                    conn.send("ERR: Math Error.".encode('utf-8'))
                else:
                    ans = float(x[1]) / float(x[2])
                    print "client want to calculate: " + str(x[1]) + "/" + str(x[2])
                    print "Send: " + str(ans)
                    conn.send("The answer is: " + str(ans).encode('utf-8'))
            except:
                conn.send("ERR: The value of x and y should be int.".encode('utf-8'))

    conn.close()
    print 'client disconnected'
