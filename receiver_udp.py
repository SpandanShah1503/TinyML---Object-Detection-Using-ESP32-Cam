import socket
import time 
import struct


#Choosing IP and Port
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

#Creating UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Socket Binding
sock.bind(UDP_IP, UDP_PORT)