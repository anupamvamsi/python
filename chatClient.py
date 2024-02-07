import socket
import threading

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 44000))


def receiveData():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            elif message == 'BYE':
                # print('bye-bye!')
                client.close()
                break
            else:
                print(message)
        except:
            print('Error')
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))


receiveDataThread = threading.Thread(target=receiveData)
receiveDataThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
