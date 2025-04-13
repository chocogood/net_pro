import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9000))
s.listen(2)

sch_num = 20221301

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    
    client.send(b'Hello ' + addr[0].encode())

    msg = client.recv(1024)
    print(msg.decode())
    
    client.send(sch_num.to_bytes(8, 'big'))
    
    client.close()
