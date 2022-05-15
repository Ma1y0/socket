from email import message
from http import client
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNET_MESSAGE = 's!disconect'
SERVER = '172.28.208.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    
print("Jestli se chcete odpojit napište s!disconect")
while True:
    message = input()
    send_message(message)