
# ? Import socket module to use network features
import socket

# ? Import the thread module to create, control and manage threads
import threading

# ? Import termcolor and it's derivatives for basic colouring 
from termcolor import *

# ? Import regex for quickly searching through strings
import re

# * VARIABLE & LIST DEFINITION START ------------------------------------------------------------------------------------------------------------------------------------------------

# ? Declare the header of 16 to add to every message so we can constantly know the length of each message
HEADER = 16

# ? Declare the port number to be '5050', which all our server and client information will go through
PORT = 5050

# ? Declare the hostname to receive the name of the server
HOSTNAME = socket.gethostname()

# ? Declare the server IP address by getting the host through hostname
SERVER_IP = socket.gethostbyname(HOSTNAME + ".local")

# ? Declare the net info of the server by placing the server address and port together
NET_INFO = (SERVER_IP, PORT)

# ? Declare the format to encode text to be "utf-8"
FORMAT = "utf-8"

# ? Declare the disconnect message to be "quit"
DISCONNECT_MESSAGE = "quit"

# ? Prototype array to store the network information of clients
addresses_proto_array = []

# ? Declare a new AF_INET socket and stream data through the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ? Bind the socket to the network information we have of the server
server.bind(NET_INFO)

# * VARIABLE & LIST DEFINITION END ------------------------------------------------------------------------------------------------------------------------------------------------

# ? Print blankspace to clear up terminal and make test look nicer
for i in range(45):
    print("")
    
clients = set()
clients_lock = threading.Lock()
    
# * HANDLE CLIENT FUNCTION DEFINITION START ------------------------------------------------------------------------------------------------------------------------------------------------

# ? Create the handle_client function with the arguments of a connection and address of the client connecting
def handle_client(conn, addr):
    
    print("")
    
    # ? Print a statement on the server side telling the address which has connected and how many active connections there currently are
    print(colored(f"[NEW CONNECTION ({threading.activeCount() - 1})] {addr} connected", "green", attrs=["bold"])) # ! Maybe have the user number be determined by amount of connections
    
    try:
        
        connected = True
        
        while connected:
            
            msg = conn.recv(1024).decode(FORMAT)
            
            if not msg:
                
                break
            
            if msg == DISCONNECT_MESSAGE:
                
                connected = False
                break
                
            print(f"[{addr}] {msg}")
            
            with clients_lock:
                
                for c in clients:

                    c.sendall(f"[{addr}] {msg}".encode(FORMAT))
            
    
    finally:
        
        with clients_lock:
            clients.remove(conn)
            
        conn.close()


































#     # ? Append the network information in string form to the prototype client network information array
#     addresses_proto_array.append(str(addr))
    
#     # ? Print the contents for debugging purposes
#     print(addresses_proto_array)
    
#     print("")
    
#     # ? Declare the connected variable and make it True
#     connected = True
    
#     # ? Create a while loop which occurs when 'connected' is True
#     while connected:
        
        
#         msg_length = conn.recv(HEADER).decode(FORMAT)
        
#         if msg_length:
            
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
            
#             if msg == DISCONNECT_MESSAGE:
                
#                 print("")
                
#                 print(colored(f"[{addr}] has disconnected", "red", attrs=["bold"]))
                
#                 disconnected = colored(f"""
# [SERVER_IP] Disconnected from {SERVER_IP}
#                 """, "red", attrs=["bold"])
                
#                 conn.send(disconnected.encode(FORMAT))
                
#                 addresses_proto_array_useable = str(addresses_proto_array)
                
#                 findAddr = re.search(str(addr), addresses_proto_array_useable)
                
#                 if findAddr:
                    
#                     findAddrIndex = addresses_proto_array.index(str(addr))
                    
#                     addresses_proto_array.pop(findAddrIndex)
                    
#                 else:
                    
#                     print(addresses_proto_array)
                
#                 connected = False
                
#             else:
                
#                 try:
                    
#                     addr1 = addresses_proto_array[0]
#                     addr2 = addresses_proto_array[1]
#                     addr3 = addresses_proto_array[2]
#                     addr4 = addresses_proto_array[3]
                    
                    
                    
#                 except:
                    
#                     pass
                
#                 msg_touchup_client = colored(f"""
# [{addr}] {msg}
#                 """, attrs=["bold"])
                
#                 msg_touchup_server = colored(f"[{addr}] {msg}", attrs=["bold"])
                
#                 print(msg_touchup_server)
                
#                 conn.send(msg_touchup_client.encode(FORMAT))
                
# #                 received = colored("""
# # [SERVER_IP] Message sent
# #                 """, "green", attrs=["bold"])
# #                 conn.send(received.encode(FORMAT))
        
#         else:
            
#             pass
            
#     conn.close()

# * HANDLE CLIENT FUNCTION DEFINITION END------------------------------------------------------------------------------------------------------------------------------------------------

def start():
    
    server.listen()
    
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    
    while True:
        
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()

print("[STARTING] Server is starting...")

start()
