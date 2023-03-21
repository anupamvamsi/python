import json
import socket
import os

# HOST = "10.1.0.78"
HOST = "127.0.0.1"
PORT = 23422


def convertToJSON(text):
    wordCount = {}
    for word in text.split():
        if wordCount.get(word, 0) == 0:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

    json_data = bytearray(str(wordCount), 'utf-8')

    json_data1 = json.dumps(wordCount, indent=4)
    json_data1 = bytearray(str(json_data1), 'utf-8')

    return json_data1


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    while True:
        clientSocket, addr = server.accept()

        with clientSocket:
            print(f"Connected by {addr}")

            while (True):
                data = clientSocket.recv(1024)
                if not data:
                    break

                converted = data.decode()

                fileName = ''
                txt = ''
                if converted[0] == '0':
                    fileName = converted[1:]

                    # returns file descriptor
                    fd = os.open(fileName, os.O_RDWR)
                    readBytes = os.read(fd, 1024)
                    convertedBytes = readBytes.decode()

                    json_data = convertToJSON(convertedBytes)

                if converted[0] == '1':
                    txt = converted[1:]
                    data = bytearray(txt, 'utf-8')
                    json_data = convertToJSON(txt)
                if converted[0] == '2':
                    data = bytearray(converted[1:], 'utf-8')
                    json_data = data

                clientSocket.sendall(json_data)
