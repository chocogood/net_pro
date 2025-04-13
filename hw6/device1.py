import socket
import random

HOST = 'localhost'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            if data == 'quit':
                print('Device1 종료')
                break
            elif data == 'Request':
                temp = random.randint(0, 40)
                humid = random.randint(0, 100)
                illum = random.randint(70, 150)
                send_data = f'Temp={temp}, Humid={humid}, Illum={illum}'
                conn.sendall(send_data.encode())
