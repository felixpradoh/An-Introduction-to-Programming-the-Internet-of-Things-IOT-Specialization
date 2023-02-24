# Use the socket to write a simple web server running on your Raspberry Pi.
# When your server receives a request it should print “Got a request!” to the screen of the Raspberry Pi.

import socket
import sys
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ms.bind(("", 1234))
except socket.error:
    print('Could NOT Bind')
    sys.exit()
    
ms.listen(5)

while True:
    conn, addr = ms.accept()
    print("Got a Request!")
    data = conn.recv(1000)
    print(data)
    if not data:
          break
    conn.sendall(data)
          
conn.close()
ms.close()

