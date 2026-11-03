import socket
import threading

HOST = "127.0.0.1"
PORT = 65433

# List to keep track of active connections
clients = []


def broadcast(message: bytes, current_conn: socket.socket):
    """Sends a message to everyone except the person who sent it."""
    for client in clients:
        if client != current_conn:
            try:
                client.sendall(message)
            except Exception:
                clients.remove(client)


def handle_client(conn: socket.socket, addr: tuple):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            # Forward the raw message bytes to all other chat members
            broadcast(data, conn)
        except Exception:
            break

    print(f"[DISCONNECTED] {addr} left.")
    clients.remove(conn)
    conn.close()


# Setup and listen loop
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Chat server running on port {PORT}...")

    while True:
        conn, addr = server.accept()
        # Spin up a dedicated thread for each client that connects
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
