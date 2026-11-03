import socket

host='127.0.0.1'
port=65432

with socket.create_connection((host,port),timeout=10) as connection:
    print("Connected to the server successfully" )
    while True:
        message =input("type a message to send or 'exit' :")
        if message.lower()=='exit':
            break

        connection.sendall(message.encode("utf-8"))
        response=connection.recv(1024)
        print(f"server echoded {response.decode('utf-8')}")