import json
import socket
import threading
import os

# HOST = "10.1.0.78"
HOST = "127.0.0.1"
PORT = 23425


def wordCounter(text):
    wordCount = {}
    for word in text.split():
        if wordCount.get(word, 0) == 0:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

    return wordCount


def convertToJSON(dictionary, indent=False):
    jsonData = json.dumps(
        dictionary, indent=4) if indent is True else json.dumps(dictionary)
    jsonData = bytearray(str(jsonData), 'utf-8')

    return jsonData


def getText(converted):
    fileName = converted
    text = converted
    try:
        fd = os.open(fileName, os.O_RDWR)

        print(f'Processing file "{fileName}"...')

        readBytes = os.read(fd, 1024)
        text = readBytes.decode()
        return text

    except:
        print(f'Processing message sent by client...')
        return text

    return {'error': 'Error. Could not process text.'}


def handleClient(clientSocket, clients):
    clientNumber = clients.index(clientSocket) + 1
    while True:
        data = clientSocket.recv(1024)
        msg = data.decode('utf-8')

        if msg == 'exit' or msg == 'stop':
            print(f'Client {clientNumber} has disconnected.')
            break
        if not data:
            print("No more data.")
            break
        if data.decode('utf-8').isspace():
            print(f'No data received from the client {clientNumber}.')
            break

        print(f"Data received from the client: {data}")
        converted = data.decode()
        text = getText(converted)

        if type(text) == dict:
            jsonData = convertToJSON(text)
        else:
            wordCount = wordCounter(text)
            jsonData = convertToJSON(wordCount, True)

        clientSocket.sendall(jsonData)
        print(f'Done. Sent word count result to client {clientNumber}.')


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    clients = []

    print(f'Server is running on {HOST}, on port {PORT}.')
    count = 0

    while True:
        clientSocket, address = server.accept()
        count += 1
        clients.append(clientSocket)

        print(f"Connected to client {count} by {address}")
        clientSocket.sendall(convertToJSON({'message': 'Connected to server'}))

        thread = threading.Thread(
            target=handleClient, args=(clientSocket, clients,))
        thread.start()
