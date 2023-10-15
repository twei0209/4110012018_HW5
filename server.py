# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 10:03:32 2023

@author: ASUS
"""

import socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',3000))
s.listen(5)

print('Echo server is listening...')

while True:
    
    conn, addr = s.accept()
    print('Connected by',addr)
    
    while True:

        data = conn.recv(1024)
        print (data)
    
    
        conn.send(data)
    
conn.close()
s.close()

