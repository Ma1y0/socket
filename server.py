import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNET_MESSAGE = 's!disconect'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[info] {addr} connect')

    connected = True

    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)

        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            
            if msg == DISCONNET_MESSAGE:
                connected = False
                break

            print(f'{addr}: {msg}')

    conn.close()

def start():
    print('[starting] server is starting.......')
    server.listen()
    print(f'[info] server is listening on {SERVER}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[info] there are {threading.active_count() - 1} conected clients right now')


task = input()

if task == 'start':
    start()