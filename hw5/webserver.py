from socket import *
import os

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    if len(req) > 0:
        request_line = req[0].split()
        if len(request_line) < 2:
            c.close()
            continue
        
        resource = request_line[1].lstrip('/')
        
        if resource == "":
            resource = "index.html"
        
        if resource in ["index.html", "iot.png", "favicon.ico"]:
            if os.path.exists(resource):
                if resource.endswith(".html"):
                    mimeType = "text/html"
                    with open(resource, 'r', encoding='utf-8') as f:
                        body = f.read()
                        c.send(f"HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n".encode() + body.encode('utf-8'))

                else:
                    mimeType = "image/png" if resource.endswith(".png") else "image/x-icon"
                    with open(resource, 'rb') as f:
                        body = f.read()
                        c.send(f"HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n".encode() + body)
            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"
                c.send(response.encode())
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"
            c.send(response.encode())
    
    c.close()
