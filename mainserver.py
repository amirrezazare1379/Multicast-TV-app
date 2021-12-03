import time

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

# tcp connection to channels for send playlist of each channel and : #

# create tcp socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , # tcp

# create host and port
HOST = "192.168.1.6"
PORT = 8989
serverSocket.bind((HOST, PORT))

# server is waiting for a channel request
serverSocket.listen(1)
print("Run Server... \n")

client, address = serverSocket.accept()

print("connected to %s " % str(address))

# recieve channel request
clientRequestMessage = client.recv(1024).decode('ascii')

# send playlist
if clientRequestMessage == messages.requestPlaylistChannel1:
    client.sendall(str(AllChannels_playList["channel1"]).encode('ascii'))

if clientRequestMessage == messages.requestPlaylistChannel2:
    client.sendall(str(AllChannels_playList["channel2"]).encode('ascii'))

if clientRequestMessage == messages.requestPlaylistChannel3:
    client.sendall(str(AllChannels_playList["channel3"]).encode('ascii'))

# check time of channel request
channelRequestTime = datetime.datetime.now().hour

# check the channels are playing :
if clientRequestMessage == messages.requestPlaylistChannel1:
    if channelRequestTime not in AllChannels_playList["channel1"]["fast and furious 10"] and channelRequestTime not in \
            AllChannels_playList["channel1"]["spyderman"]:
        client.sendall(messages.channel1IsNotPlaying.encode('ascii'))
    else:
        client.sendall(messages.channel1IsPlaying.encode('ascii'))

if clientRequestMessage == messages.requestPlaylistChannel2:
    if channelRequestTime not in AllChannels_playList["channel2"]["venom"] and channelRequestTime not in \
            AllChannels_playList["channel2"]["spyderman"]:
        client.sendall(messages.channel2IsNotPlaying.encode('ascii'))
    else:
        client.sendall(messages.channel2IsPlaying.encode('ascii'))

if clientRequestMessage == messages.requestPlaylistChannel3:
    if channelRequestTime not in AllChannels_playList["channel3"]["fast and furious 10"] and channelRequestTime not in \
            AllChannels_playList["channel3"]["venom"]:
        client.sendall(messages.channel3IsNotPlaying.encode('ascii'))
    else:
        client.sendall(messages.channel3IsPlaying.encode('ascii'))

requestWatchFlagChannel1 = False
requestWatchFlagChannel2 = False
requestWatchFlagChannel3 = False

import json

# recv ack or nack for watching
ackOrNack = client.recv(1024).decode('ascii')
if ackOrNack.lower() == messages.NO:
    print('tcp connection closed.')
    client.close()

# udp setting for channel 1 :
if ackOrNack.lower() == messages.YES and clientRequestMessage == messages.requestPlaylistChannel1:
    requestWatchFlagChannel1 = True
    print(" sending image ...")
    # client.close()
    print("strar udp connection ...")
    time.sleep(3)
    # SENDER
    import socket

    group = '224.1.1.1'
    port = 5004
    # 2-hop restriction in network
    ttl = 1
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_TTL,
                    ttl)
    sock.sendto(b'hello udp client', (group, port))

    # if channelRequestTime in AllChannels_playList["channel1"]["fast and furious 10"]:
    #     for imgNumber in range(0, 100, 5):
    #         f = open(f"./save/fast/{imgNumber}.png", "r")
    #         f = f.read()
    #         sock.sendto(str(f), (group, port))
    # elif channelRequestTime in AllChannels_playList["channel1"]["spyderman"]:
    #     for imgNumber in range(0, 100, 5):
    #         f = open(f"./save/spyderman/{imgNumber}.png", "r")
    #         f = f.read()
    #         sock.sendto(str(f), (group, port))

# ======================================================


# udp setting for channel 2 :
if ackOrNack.lower() == messages.YES and clientRequestMessage == messages.requestPlaylistChannel2:
    requestWatchFlagChannel2 = True
    print(" sending image ...")
    # client.close()
    print("strar udp connection ...")
    time.sleep(3)
    # SENDER
    import socket

    group = '224.1.1.1'
    port = 5004
    # 2-hop restriction in network
    ttl = 1

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_TTL,
                    ttl)

    sock.sendto(b'hello udp client', (group, port))

    # if channelRequestTime in AllChannels_playList["channel2"]["venom"]:
    #     with open('./save/venom/0.png', 'rb') as f:
    #         client.send(f.read())
    #         l = f.read()
    #         # im = Image.open(l)
    #         # im.show()
    #         f.close()

    # import json
    # import base64
    # data = {}
    # with open('./save/venom/0.png', mode='rb') as file:
    #     img = file.read()
    # data['img'] = base64.b64encode(img)
    # sock.sendto(json.dumps(data), (group, port))
    # import base64
    # import json
    # import cv2
    #
    # for i in range(0,100,5):
    #     img = cv2.imread(f'./save/fast/{i}.png')
    #     string = base64.b64encode(cv2.imencode('.png', img)[1]).decode()
    #     dict = {
    #         'img': string
    #     }
    #     with open(f'./jsonImage/{i}.json', 'w') as outfile:
    #         json.dump(dict, outfile, ensure_ascii=False, indent=4)

    #
    # elif channelRequestTime in AllChannels_playList["channel2"]["spyderman"]:
    #     import json
    #     import base64
    #     data = {}
    #     with open('./save/spyderman/0.png', mode='rb') as file:
    #         img = file.read()
    #     data['img'] = base64.b64encode(img)
    #     sock.sendto(json.dumps(data), (group, port))

# ============================================================================

import cv2

# udp setting for channel 3 :
if ackOrNack.lower() == messages.YES and clientRequestMessage == messages.requestPlaylistChannel3:
    requestWatchFlagChannel3 = True
    print(" sending image ...")
    # client.close()
    print("strar udp connection ...")
    time.sleep(3)
    # SENDER
    import socket

    group = '224.1.1.1'
    port = 5004
    # 2-hop restriction in network
    ttl = 1

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM,
                         socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_TTL,
                    ttl)

    sock.sendto(b'hello udp client', (group, port))

    # # udpSendImage()
    # # SENDER
    # group = '224.1.1.1'
    # port = 5004
    # # 1-hop restriction in network
    # ttl = 1
    # sock = socket.socket(socket.AF_INET,
    #                      socket.SOCK_DGRAM,
    #                      socket.IPPROTO_UDP)
    # sock.setsockopt(socket.IPPROTO_IP,
    #                 socket.IP_MULTICAST_TTL,
    #                 ttl)

    # if channelRequestTime in AllChannels_playList["channel3"]["fast and furious 10"]:
    #
    #
    #
    #
    #
    # elif channelRequestTime in AllChannels_playList["channel3"]["venom"]:
