import socket
import threading
import sys

HOST = "127.0.0.1"
# HOST = "10.1.0.78"
PORT = 23425


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def sendDataToServer(data=''):
    while True:
        try:
            data = client.recv(1024)
            print(data.decode('utf-8'))
            msg = input('Message or file name: ')

            if msg == 'exit' or msg == 'stop':
                client.sendall(msg.encode('utf-8'))
                client.close()
                break

            client.sendall(msg.encode('utf-8'))
        except Exception as e:
            print("ERROR:", e)
            client.close()
            break


if __name__ == "__main__":
    sendDataToServer()
