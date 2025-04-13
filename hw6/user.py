import socket
import time

DEVICE1_ADDR = ('localhost', 9001)
DEVICE2_ADDR = ('localhost', 9002)

def connect_device(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)
    return s

def write_to_file(device_name, data):
    now = time.ctime()  # 현재 시간 문자열
    with open('data.txt', 'a') as f:
        f.write(f'{now}: {device_name}: {data}\n')

def main():
    sock1 = connect_device(DEVICE1_ADDR)
    sock2 = connect_device(DEVICE2_ADDR)
    
    count1 = 0
    count2 = 0

    while True:
        user_input = input("1: Device1, 2: Device2, quit: 종료 >> ").strip()
        if user_input == '1' and count1 < 5:
            sock1.sendall(b'Request')
            data = sock1.recv(1024).decode()
            write_to_file('Device1', data)
            count1 += 1
        elif user_input == '2' and count2 < 5:
            sock2.sendall(b'Request')
            data = sock2.recv(1024).decode()
            write_to_file('Device2', data)
            count2 += 1
        elif user_input == 'quit':
            sock1.sendall(b'quit')
            sock2.sendall(b'quit')
            sock1.close()
            sock2.close()
            break
        else:
            print("잘못 입력했거나 수집 횟수를 초과했어.")

if __name__ == '__main__':
    main()
