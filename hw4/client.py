from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('calculation: ')
    if msg.lower() == 'q':
        s.send(msg.encode())
        break
    
    s.send(msg.encode())
    result = s.recv(1024).decode()
    print('Result:', result)

s.close()