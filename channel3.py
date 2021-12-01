#tcp connection for reciev the playlist off channels
import socket
import messages

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , # tcp

s.connect(("192.168.1.6", 8989))
sendMsg1 = messages.requestPlaylistChannel3
s.sendall(sendMsg1.encode('ascii'))

revcMsg = s.recv(1024)
print(revcMsg.decode('ascii'))


revcMsg = s.recv(1024)
print(revcMsg.decode('ascii'))

s.close()