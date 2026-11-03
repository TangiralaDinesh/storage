import socket

host="google.com" 
port=80

request=(
    f"GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n\r\n"
).encode("ascii")

chunks=[]
with socket.create_connection((host,port),timeout=10) as connection:
    connection.sendall(request)
    while chunk := connection.recv(4096):
        chunks.append(chunk)

response =b"".join(chunks);
print(response.decode("utf-8",errors="ignore"))
