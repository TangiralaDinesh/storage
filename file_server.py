import socket 
host ="127.0.0.1"
port=65534
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server :
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen()
    print(f"Server listening on port {port}")

    conn,addr =server.accept()
    with conn ,open("received.txt","wb") as file:
        while True:
            chunk=conn.recv(4096)
            if not chunk:
                break
            file.write(chunk)
print("File successfully recieved and saved as'recieved.txt ")
