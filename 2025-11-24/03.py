import socket

IP = '192.168.9.111'
PORT = 8888
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((IP,PORT))

data=client.recv(1024)
print("data1: ",data.decode('utf-8'))
client.send("sss".encode('utf-8'))
data=client.recv(1024)
print("data2: ",data.decode('utf-8'))
client.close