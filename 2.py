import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connect to the server
s.connect((host, port))

# send messages to the server
while True:
  message = input("Type a message: ")
  s.send(message.encode())
  if message == "exit":
    break

# close the connection
s.close()
