import messages
import socket
import datetime

# set the channels playlist:

AllChannels_playList = {
    "channel1": {
        "fast and furious 10": [0, 1, 2, 3],
        "spyderman": [12, 13, 14, 15]
    },
    "channel2": {
        "venom": [4, 5, 6, 7],
        "spyderman": [16, 17, 18, 19]
    },
    "channel3": {
        "fast and furious 10": [8, 9, 10, 11],
        "venom": [20, 21, 22, 23]
    }
}

### tcp connection to channels for send playlist of each channel and :

# create tcp socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , # tcp

# create host and port
s.bind(("192.168.1.6", 8989))

# server is waiting for a channel request
s.listen(1)

print("Run Server... \n")

c, addr = s.accept()

print("connect to %s " % str(addr))

# recieve channel request
cmsg = c.recv(1024).decode('ascii')

# check that which channel sends request for recieve playlist
if cmsg == messages.requestPlaylistChannel1:
    c.sendall(str(AllChannels_playList["channel1"]).encode('ascii'))

if cmsg == messages.requestPlaylistChannel2:
    c.sendall(str(AllChannels_playList["channel2"]).encode('ascii'))

if cmsg == messages.requestPlaylistChannel3:
    c.sendall(str(AllChannels_playList["channel3"]).encode('ascii'))

# check time of channel request
time = datetime.datetime.now().hour

# check the channels are playing :
if cmsg == messages.requestPlaylistChannel1:
    if time not in AllChannels_playList["channel1"]["fast and furious 10"] and time not in \
            AllChannels_playList["channel1"]["spyderman"]:
        errMsg = "channel1 is not playing !!!"
        c.sendall(errMsg.encode('ascii'))

if cmsg == messages.requestPlaylistChannel2:
    if time not in AllChannels_playList["channel2"]["venom"] and time not in AllChannels_playList["channel2"][
        "spyderman"]:
        errMsg = "channel2 is not playing !!!"
        c.sendall(errMsg.encode('ascii'))

if cmsg == messages.requestPlaylistChannel3:
    if time not in AllChannels_playList["channel3"]["fast and furious 10"] and time not in \
            AllChannels_playList["channel3"]["venom"]:
        errMsg = "channel3 is not playing !!!"
        c.sendall(errMsg.encode('ascii'))

c.close()

# =======================================================================================================
# =======================================================================================================


### Multicast UDP send image

# SENDER

import socket
group = '224.1.1.1'
port = 5004

# 2-hop restriction in network
ttl = 2

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)

sock.sendto(b"hello world", (group, port))
