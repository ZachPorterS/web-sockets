import socket

HOST = "127.0.0.1"  # Standard Loop Back Address (localhost)
PORT = 65432  # Port to listen on (non-privledged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((HOST, PORT))
    stream.listen()

    # Create the connection, and set the address of connection
    connection, address = stream.accept()

    # Loop through the connection, printing out the
    # address at which the connection is made
    with connection:
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
