import socket

# 서버 주소 설정
SERVER_HOST = 'localhost'
SERVER_PORT = 9999

# UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('Enter the message("send mboxId message" or "receive mboxId"):')
    client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

    if message.lower() == 'quit':
        break

    response, _ = client_socket.recvfrom(1024)
    print(response.decode())

client_socket.close()
