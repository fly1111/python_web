def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
 '''
 #client.py


import socket

#实例化

client = socket.socket()

ip_port = ('127.0.0.1',8888)
client.connect(ip_port)
while True:
    #接收数据
    data = client.recv(1024) 
    print(data.decode())
    msg_input = input("请输入发送消息:")
    client.send(msg_input.encode())
    if msg_input == 'exit':
        break
    data = client.recv(1024)
    print(data.decode())
 '''
