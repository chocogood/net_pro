import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break

def main():
    host = 'localhost'
    port = 2500

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 연결 시도에 대한 예외 처리
    try:
        sock.connect((host, port))
    except ConnectionRefusedError:
        print(f"[오류] 서버({host}:{port})에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
        return
    except Exception as e:
        print(f"[예외 발생] {e}")
        return

    my_id = input("ID를 입력하세요: ")
    sock.send(f"[{my_id}]".encode())

    recv_thread = threading.Thread(target=receive, args=(sock,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        msg = input()
        if msg.lower() == 'quit':
            sock.send(f"[{my_id}] 님이 퇴장하셨습니다.".encode())
            break
        sock.send(f"[{my_id}] {msg}".encode())

    sock.close()

if __name__ == "__main__":
    main()
