import socket
import sys

default_timeout = 3
address = sys.argv[1]
port = int(sys.argv[2])

try:
    timeout = int(sys.argv[3])
except IndexError:
    timeout = int(default_timeout)

sock = socket.socket()
sock.settimeout(timeout)

try:
    sock.connect((address, port))
    print(0)
except Exception as e:
    print(1)
# print(f'something wrong with {address} {port}. Exception is {e}')
finally:
    sock.close()
