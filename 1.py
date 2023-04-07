import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host, and a well-known port
s.bind((host, port))

# become a server socket
s.listen(5)

print("Server listening on {}:{}".format(host, port))

# wait for a connection
conn, addr = s.accept()

print("Connected by", addr)

# keep receiving messages from the client
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received message:", data)

# close the connection
conn.close()
