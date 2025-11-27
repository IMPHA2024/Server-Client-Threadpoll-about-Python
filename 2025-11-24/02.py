# server build->bind->listen->accept->read/send->close
# client build->require->read/send->close
import socket

IP = '0.0.0.0'
PORT = 8888
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((IP , PORT))
server.listen(5)
print("listen")

running = True
while running:
    try:
        client , addr = server.accept()
        client.send("connect".encode('utf-8'))
        print("connect")
        data = client.recv(1024)
        if data.decode('utf-8') == 'exit':
            print("close connent")
            running = False
        else:
            print(f"收到客户端 {addr} 的消息：{data.decode('utf-8')}")
            client.send(f"已收到你的消息：{data.decode('utf-8')}".encode('utf-8'))
        client.close()
    except BlockingIOError:
        print("no blocking")
        pass
    except Exception as e:
        print("error : {e}")
server.close()