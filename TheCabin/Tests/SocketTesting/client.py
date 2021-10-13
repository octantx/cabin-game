import socket
import sys
import time
from termcolor import *
from threading import Thread,Lock

HEADER = 16
PORT = 5050
HOSTNAME = socket.gethostname()
SERVER = socket.gethostbyname(HOSTNAME + ".local")
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "quit"
ADDR = (SERVER, PORT)

class globalVars():
    pass

G = globalVars()
G.lock = Lock() 
G.value = 0
G.kill = False

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)
    
connection = connect()

def main():

    def get_message():
        
        msg = connection.recv(1024).decode(FORMAT)
        
        print(f"""

{msg}
        """)
        
        main()
        
    def start():
        
        while True:
            
            t = Thread(target=get_message)
            t.start()
            
            msg = input("Message: ")
            
            if msg == "q":
                
                send(connection, DISCONNECT_MESSAGE)
                time.sleep(1)
                print("Disconnected")
            
            send(connection, msg)

    start()
    
main()










































# for i in range(45):
#     print("")
    
# print(colored("""
#  ▄██████▄     ▄███████▄ ███    █▄   ▄█          ▄████████ ███▄▄▄▄    ▄████████    ▄████████ 
# ███    ███   ███    ███ ███    ███ ███         ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ 
# ███    ███   ███    ███ ███    ███ ███         ███    █▀  ███   ███ ███    █▀    ███    █▀  
# ███    ███   ███    ███ ███    ███ ███        ▄███▄▄▄     ███   ███ ███         ▄███▄▄▄     
# ███    ███ ▀█████████▀  ███    ███ ███       ▀▀███▀▀▀     ███   ███ ███        ▀▀███▀▀▀     
# ███    ███   ███        ███    ███ ███         ███    █▄  ███   ███ ███    █▄    ███    █▄  
# ███    ███   ███        ███    ███ ███▌    ▄   ███    ███ ███   ███ ███    ███   ███    ███ 
#  ▀██████▀   ▄████▀      ████████▀  █████▄▄██   ██████████  ▀█   █▀  ████████▀    ██████████ 
#                                    ▀
#                                    - Network Prototype -
# """, "yellow", attrs=["bold"]))

# print(colored("Type \"help\" for a list of commands!", attrs=["bold"]))

# print("")

# def send(msg):
    
#     try:
    
#         message = msg.encode(FORMAT)
#         msg_length = len(message)
#         send_length = str(msg_length).encode(FORMAT)
#         send_length += b" " *  (HEADER - len(send_length))
#         client.send(send_length)
#         client.send(message)
#         print(client.recv(2048).decode(FORMAT))
        
#     except:
        
#         sys.exit()

# def packet_send():
    
#     try:
        
#         pack = str(input("> "))
        
#         if pack == "help":
            
#             print("""
#     quit: disconnects from the server
#             """)
            
#             packet_send()
            
#         elif pack == "quit":
        
#             send(pack)
            
#             sys.exit()
            
#         else:
        
#             send(pack)
        
#             packet_send()
        
#     except:
        
#         pack = "quit"
        
#         send(pack)
        
#         sys.exit()

# packet_send()