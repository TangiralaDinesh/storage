import socket
import threading

HOST = "127.0.0.1"
PORT = 65433

name = input("Enter your username: ")


def receive_messages(client_socket: socket.socket):
    """Listens continuously for messages from the server on a background thread."""
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(message)
        except Exception:
            print("Disconnected from server.")
            break


# Connect and start the background listening process
with socket.create_connection((HOST, PORT)) as client:
    print(f"Connected to chat as {name}!")

    # Start the listening thread so incoming text prints while you type
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    # Main thread handle text input
    while True:
        msg = input()
        if msg.lower() == "exit":
            break

        formatted_msg = f"{name}: {msg}"
        client.sendall(formatted_msg.encode("utf-8"))

