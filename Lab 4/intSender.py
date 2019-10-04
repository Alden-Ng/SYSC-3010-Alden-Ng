
# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import random

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

print ("Enter a value for N")
N = sys.stdin.readline().strip()
#    s.sendall(data.encode('utf-8'))
for i in range(int(N)):
    s.sendto(str(random.randint(1,1000)).encode('utf-8'), server_address)
quit()


