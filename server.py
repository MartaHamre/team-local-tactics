from socket import socket


sock = socket()

sock.bind(("localhost", 5555))

sock.listen()
print("Connection pending, please wait.")

while True:
    sock.accept()
    print("Server connected!")

    ###
    
    sock.close()