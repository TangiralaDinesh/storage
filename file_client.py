import socket
host="127.0.0.1"
port=65534
with open("sendme.txt","rb") as file ,socket.create_connection((host,port))as client:
    print("sending file data....")

    while chunk:=file.read(4096):
        client.sendall(chunk)
print("file transfer complete")