import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())
    
sock.send('Yewon Kim'.encode())

sch_num = sock.recv(1024)
recv_sch_num = int.from_bytes(sch_num, 'big')
print(recv_sch_num)

sock.close()