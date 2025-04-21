from socket import *
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        send_msg = str(reTx) + ' ' + msg
        sock.sendto(send_msg.encode(), ('localhost', port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            print(f'⏱️ 재전송 {reTx + 1}회...')
            reTx += 1
            continue
        except ConnectionResetError as e:
            print('서버로부터 연결이 거부됨:', e)
            break
        else:
            break

    sock.settimeout(None)

    while True:
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
        except ConnectionResetError as e:
            print('연결 오류:', e)
            break
