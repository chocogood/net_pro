from socket import *
import re

def calculate(expression):
    try:
        match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", expression)
        if match:
            num1 = int(match.group(1))  
            operator = match.group(2)     
            num2 = int(match.group(3))  

            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                if num2 == 0:
                    return "Error: Division by zero"
                return round(num1 / num2, 1)
        else:
            return "Invalid expression"
    except Exception as e:
        return f"Error: {str(e)}"

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(1)
print('waiting...')

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    
    while True:
        data = client.recv(1024)
        if not data:
            break
        expression = data.decode().strip()
        if expression.lower() == 'q':
            break

        result = calculate(expression)
        client.send(str(result).encode())

    client.close()
