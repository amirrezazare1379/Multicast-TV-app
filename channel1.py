# tcp connection for reciev the playlist off channels
import socket
import messages

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , # tcp
s.connect(("192.168.1.6", 8989))
sendMsg1 = messages.requestPlaylistChannel1
s.sendall(sendMsg1.encode('ascii'))

revcMsg = s.recv(1024)
print(revcMsg.decode('ascii'))

revcMsg = s.recv(1024)
print(revcMsg.decode('ascii'))

s.close()



#=======================================================================

# RECEIVER
# Multicast UDP image recieve

import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5004

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print(sock.recv(10240))
