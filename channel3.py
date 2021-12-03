# tcp connection for reciev the playlist off channels
import socket
import messages

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , # tcp
HOST = "192.168.1.6"
PORT = 8989
clientSocket.connect((HOST, PORT))
requestMessagge = messages.requestPlaylistChannel3
clientSocket.sendall(requestMessagge.encode('ascii'))

# reciev playlist
rcvPlaylistMessage = clientSocket.recv(1024)
print(rcvPlaylistMessage.decode('ascii'))

# recv msg that channel is playing ro not
channelStatus = clientSocket.recv(1024)
channelStatus = channelStatus.decode('ascii')
if channelStatus == messages.channel3IsNotPlaying:
    print(channelStatus)
elif channelStatus == messages.channel3IsPlaying:
    print(channelStatus)
    ackOrNack = input(messages.wantToWatch)
    clientSocket.sendall(ackOrNack.encode('ascii'))

clientSocket.close()




#UDP


# RECEIVER

print("start udp ...")
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

