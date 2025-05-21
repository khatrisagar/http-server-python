import socket

HOST = "127.0.0.1"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server is running on http://{HOST}:{PORT}")

client_socket, client_address = server_socket.accept()
print(f"Connection received from {client_address}")

request_data = client_socket.recv(1024).decode("utf-8")
print("=== HTTP Request ===")
print(request_data)

response = (
    "HTTP/1.1 200 OK\r\n" "Content-Type: text/html\r\n" "\r\n" "<h1>Hello, World!</h1>"
)
client_socket.sendall(response.encode("utf-8"))

client_socket.close()
server_socket.close()
