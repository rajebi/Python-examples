	
print ("hello world")

#=============================================
#                Sockets
#
#     Socket server example in python
#=============================================
 
import socket   #for sockets
import sys  	#for exit
import _thread


host = 'localhost'	# Symbolic name, meaning all available interfaces
port = 8888 		# Arbitrary non-privileged port

#--------------------------------------
#create an AF_INET, STREAM socket (TCP)
#--------------------------------------
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

#------------------------------------------------
# Start listening on socket for client connection
#------------------------------------------------
# The parameter of the function listen is called backlog. It controls the number 
# of incoming connections that are kept "waiting" if the program is already busy. 
# So by specifying 10, it means that if 10 connections are already waiting 
# to be processed, then the 11th connection request shall be rejected. This will 
# be more clear after checking socket_accept.
s.listen(10)
print ("Socket now listening")

#-------------------------------------- 
# accept connection from client client
#--------------------------------------
# wait to accept a connection - blocking call: waits till client shows up
conn, addr = s.accept()
print ("Connected with " + addr[0] + ":" + str(addr[1]))

#--------------------------------- 
# now keep talking with the client
#---------------------------------
# infinite loop so that function do not terminate and thread do not end.
while True:
	print ("waiting to receive data from client")
	#Receiving from client
	data = conn.recv(1024)
	print ("data received from client:  " + data.decode('utf-8'))
	#print(data.decode('utf-8')) # print received data
	
	if (data.decode('utf-8')) == 'end':
		print("end rcvd, closing connection")
		break
	
	reply = "OK..." + data.decode('utf-8')
	if not data: 
		print("no data, closing connection")
		break
	
	conn.sendall(reply.encode('utf-8'))
 
#came out of loop
conn.close()


#---------------------------------------- 
# Code for connecting to multiple client
#----------------------------------------
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
		print ("waiting to receive data from client")
        #Receiving from client
		data = conn.recv(1024)
		print ("data received from client")
		print(data.decode('utf-8')) # print received data
		
		if (data.decode('utf-8')) == 'end':
			break
		
		reply = "OK..." + data.decode('utf-8')
		if not data: 
			print("no data, closing connection")
			break
        
		conn.sendall(reply.encode('utf-8'))
     
    #came out of loop
	conn.close()

# This while loops waits for new client connections. If you are going to use just one client
# then, you don't need this while loop
##while 1:
    #wait to accept a connection - blocking call
	
	# Including the following 1 line of code makes the server connet to multiple clients
    ## conn, addr = s.accept()
    ## print ("Connected with " + addr[0] + ":" + str(addr[1]))
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    ##_thread.start_new_thread(clientthread ,(conn,))
     
s.close()





