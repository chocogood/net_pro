import socket
import threading
import time

clients = []  # 접속 중인 모든 클라이언트 소켓 저장 리스트
lock = threading.Lock()  # 스레드 간 동기화를 위한 Lock

def broadcast(msg, sender):
    with lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(msg)
                except:
                    pass

def handle_client(client_sock, addr):
    print(f"New client connected: {addr}")
    with lock:
        clients.append(client_sock)

    try:
        while True:
            data = client_sock.recv(1024)
            if not data:
                break
            timestamp = time.strftime('%a %b %d %H:%M:%S %Y')
            print(f"{timestamp} {addr}: {data.decode()}")
            broadcast(data, client_sock)
    except:
        pass
    finally:
        with lock:
            clients.remove(client_sock)
        client_sock.close()
        print(f"Client disconnected: {addr}")

def main():
    host = 'localhost'
    port = 2500
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(5)
    print("Chat server started.")

    while True:
        client_sock, addr = server_sock.accept()
        t = threading.Thread(target=handle_client, args=(client_sock, addr))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    main()
