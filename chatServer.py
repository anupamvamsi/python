import socket
import threading

HOST = '127.0.0.1'
PORT = 44000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast(msg):
    for clientSocket in clients:
        clientSocket.send(msg)


def handleClient(clientSocket):
    while True:
        try:
            # if not clientSocket._closed:
            #     print(clientSocket, clients)
            msg = clientSocket.recv(1024)
            broadcast(msg)
            # print('bye???')

            # if 'bye' in msg.decode('utf-8'):
            #     print('bye?')

            #     index = clients.index(clientSocket)
            #     nickname = nicknames[index]
            #     broadcast(f'{nickname} says bye!'.encode('utf-8'))

            #     msg = f'{nickname} has left the chat.'.encode('utf-8')
            #     broadcast(msg)
            #     clientSocket.send('BYE'.encode('utf-8'))
            #     clients.remove(clientSocket)
            #     clientSocket.close()
            #     nicknames.remove(nickname)
            #     break
        except:
            index = clients.index(clientSocket)
            clients.remove(clientSocket)
            clientSocket.close()
            nickname = nicknames[index]
            msg = f'{nickname} has left the chat.'.encode('utf-8')
            nicknames.remove(nickname)
            break


def receiveClientConnection():
    while True:
        clientSocket, address = server.accept()
        print("clientSocket, address: ", clientSocket, address)
        print(f'Connected with {str(address)}.')

        clientSocket.send('NICK'.encode('utf-8'))
        nickname = clientSocket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(clientSocket)

        print(f'Nickname of the new client is {nickname}.')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))

        clientSocket.send('Connected to the server.'.encode('utf-8'))

        thread = threading.Thread(target=handleClient, args=(clientSocket,))
        thread.start()


# if __name__ == "__main__":
receiveClientConnection()
