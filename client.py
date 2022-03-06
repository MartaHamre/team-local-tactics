from socket import socket


sock = socket()

target_address = ("localhost", 5555)
sock.connect(target_address) 

sock.close()