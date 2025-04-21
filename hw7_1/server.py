from socket import *
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)

    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        sock.sendto(b'ack', addr)
        print('<-', data.decode())
        break

    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            print(f'⏱️ 재전송 {reTx + 1}회...')
            reTx += 1
            continue
        except ConnectionResetError as e:
            print('연결이 강제로 끊어졌습니다:', e)
            break
        else:
            break
