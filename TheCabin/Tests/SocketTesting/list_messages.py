import socket
import sys
import time
from termcolor import *

HEADER = 16
PORT = 5050
HOSTNAME = socket.gethostname()
SERVER = socket.gethostbyname(HOSTNAME + ".local")
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "quit"
ADDR = (SERVER, PORT)

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)
        
start()