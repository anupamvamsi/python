# TCP Connections/ Network/Internet sockets
# Process (browser) <- Internet -> Process (web server)

# TCP Ports: Application-specific / process-specific

# https://docs.python.org/3/howto/sockets.html
# INET = IPv4
# STREAM = TCP
# Sockets = Blocking, Non-blocking
#         = Client, Server
#           Client application == only client sockets
#           Web server         == both client and server sockets

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('wiki.qt.io', 80))

'''
# IMPORTANT
# \r\n = carriage return or EOL in Windows
# \n   = EOL in other systems
# \r\n\r\n (Windows)  (or) \n\n (Other) = indicates nothing in between two EOL sequences
'''

# Use in Windows
cmd_win10 = 'GET http://wiki.qt.io/Books HTTP/1.1\r\nHost:wiki.qt.io\r\n\r\n'.encode()
# cmd_win10 = 'GET https://www.python.org HTTPS/1.0\r\n\r\n'.encode()

# Use in Linux and other systems
cmd_linux = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

my_socket.send(cmd_win10)

while True:
    data = my_socket.recv(4096)
    if len(data) < 1:
        break
    print(data.decode())

my_socket.close()
