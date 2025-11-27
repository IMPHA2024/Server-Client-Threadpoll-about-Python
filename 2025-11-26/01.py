import threading
import socket

IP = '192.168.9.111'
PORT = 8888


def connect():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((IP,PORT))
    data=client.recv(1024)
    print("data1: ",data.decode('utf-8'))
    client.send("sss".encode('utf-8'))
    client.close

def test():
    for _ in range(10):
        t = threading.Thread(target=connect)
        t.start()

test()