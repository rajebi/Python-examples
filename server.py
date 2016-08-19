	
print ("hello world")

#=============================================
#                Sockets
#
#     Socket server example in python
#=============================================
 
import socket   #for sockets
import sys  	#for exit
import _thread


host = 'localhost'# Symbolic name, meaning all available interfaces
port = 8888 # Arbitrary non-privileged port

#-------------------------------------
#create an AF_INET, STREAM socket (TCP)
#-------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (" Client Socket is Created")

#----------------------------------
# Bind socket to local host
#----------------------------------
try:
    s.bind((host, port))
except socket.error as msg:
    print ("Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
    sys.exit()
	
print (" Socket bind completed")

#---------------------------
# Start listening on socket
#---------------------------
s.listen(10)
print ("Socket now listening")

#-----------------------------
# handle clients
#-----------------------------
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
	#welcomeMessage = 'Welcome to the server. Type something and hit enter\n'
	#conn.send(welcomeMessage.encode('utf-8')) #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
	while True:
         
        #Receiving from client
		data = conn.recv(1024)
		print(data.decode('utf-8')) # print received data
		
		if (data.decode('utf-8')) == 'end':
			break
		
		reply = "OK..." + data.decode('utf-8')
		if not data: 
			break
        
		conn.sendall(reply.encode('utf-8'))
     
    #came out of loop
	conn.close()


#--------------------------------- 
# now keep talking with the client
#---------------------------------
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ("Connected with " + addr[0] + ":" + str(addr[1]))
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    _thread.start_new_thread(clientthread ,(conn,))
     
s.close()





