# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:12:43 2023

@author: ASUS
"""

import socket 

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 3000)
conn.connect(server_address)

message = input("Enter a message to send to the server:")

while True:
    conn.send(message.encode())
    
    data = conn.recv(1024)
    print(f"Received from server: {data.decode()}")
    
conn.close()
