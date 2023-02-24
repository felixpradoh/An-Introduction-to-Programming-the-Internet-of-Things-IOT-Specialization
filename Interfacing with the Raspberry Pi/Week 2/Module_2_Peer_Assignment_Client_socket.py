import socket
import sys

try:
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed creating a socket!')
    sys.exit()

print(ms)
host = 'GatxanPi'
print(host)

try:
    ms.connect((host, 1234))
    print('Connection Succesful')
except:
    print('Cannot connect to the host')
    sys.exit()


message = b"Hello to my Rpi"
