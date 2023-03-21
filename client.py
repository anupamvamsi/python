import socket
import sys

HOST = "127.0.0.1"
# HOST = "10.1.0.242"
PORT = 23422

if len(sys.argv) == 2:
    msg = '0' + sys.argv[1]
elif len(sys.argv) > 2:
    sys.argv[1] = '1' + sys.argv[1]
    msg = sys.argv[1:]
    msg = ' '.join(msg)
else:
    msg = "2Please specify a filename or a string of characters."

msg = bytearray((msg), 'utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall(msg)
    data = client.recv(1024)

print("Received from the server: ", data.decode())
