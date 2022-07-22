import re
import socket

my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_server.bind(('127.0.0.1', 5000))
my_server.listen(5)

response = """HTTP/1.1 200 OK
Content-Length: 100
Connection: close

<!DOCTYPE html>
<html>
<body>
nice to see this text line!
</body>
</html>



"""

while True:
    print("accepting...")
    conn, addr = my_server.accept()
    # print(conn)
    # print(addr)
    data = conn.recv(2048).decode('utf-8')
    print(data)
    if re.match("GET", data):
        conn.send(response.encode('utf-8'))

# 数据能发，就是浏览器不解析，这个就是HTTP报文结构的问题了
