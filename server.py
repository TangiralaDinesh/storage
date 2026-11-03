import socket
host="127.0.0.1"
port=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen()
    print(f"Server is waiting for connection on port {port}....")
    conn ,addr =server.accept()
    with conn :
        print(f"Connected successfully to ; {addr}")
        while True:
            data=conn.recv(1024)
            if not data :
                break
            print(f"Recived from Client : {data.decode('utf-8') }")
            conn.sendall(data)
            