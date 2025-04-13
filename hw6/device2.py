import socket
import random

HOST = 'localhost'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            if data == 'quit':
                print('Device2 종료')
                break
            elif data == 'Request':
                heartbeat = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                send_data = f'Heartbeat={heartbeat}, Steps={steps}, Cal={cal}'
                conn.sendall(send_data.encode())
