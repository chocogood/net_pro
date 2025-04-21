import socket

# 서버 설정
HOST = 'localhost'
PORT = 9999

# 메시지 박스 저장용 딕셔너리
message_boxes = {}

# UDP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"UDP 서버가 {HOST}:{PORT}에서 시작되었습니다.")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode().strip()

    if message.lower() == 'quit':
        print("클라이언트가 종료 요청을 보냈습니다.")
        break

    elif message.startswith("send "):
        parts = message.split(' ', 2)
        if len(parts) < 3:
            server_socket.sendto("Invalid send command".encode(), addr)
            continue
        mbox_id, msg = parts[1], parts[2]
        if mbox_id not in message_boxes:
            message_boxes[mbox_id] = []
        message_boxes[mbox_id].append(msg)
        server_socket.sendto("OK".encode(), addr)

    elif message.startswith("receive "):
        parts = message.split(' ', 1)
        if len(parts) != 2:
            server_socket.sendto("Invalid receive command".encode(), addr)
            continue
        mbox_id = parts[1]
        if mbox_id in message_boxes and message_boxes[mbox_id]:
            response = message_boxes[mbox_id].pop(0)
            server_socket.sendto(response.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)
    else:
        server_socket.sendto("Invalid command".encode(), addr)

server_socket.close()
print("서버 준비 완료. 메시지를 기다립니다...")
