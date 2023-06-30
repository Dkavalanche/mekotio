# Simula un C&C para interactuar con un BOT Mekotio en una red controlada
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        self.data = self.request.recv(2048).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(b'<|WY|>')
        #self.request.sendall(b'orca3whiid8gota@<|iuqm|>')
        self.data = self.request.recv(2048).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        
if __name__ == "__main__":
    HOST, PORT =  "localhost", 6742

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:

        server.serve_forever()

#<|SNUNFHXQU|>
#<|WY|> / Pregunta nombre de bot.
#<|xywz|>1--09-06-N-96<|>32 - Windows 8.16.39600<|>TEMPO tempo123 windows defender-gaalicia<|>TEMPO tempo123<<|6//&M31R543V36m!galicia
#<|stygqwokui|>8259478<<|<|iuqm|>
#<|ywloz|><|dlpeaUoilF|>galiciaxx.zip<<|67547<|iuqm|>
#<|SLUT|><|Eoadivn|>###TEMPO
#orca3whiid8gota@<|iuqm|>  bloquea

#hxxp[:]//serviceares[.]hopto[.]org/contig.txt
#automovilespalma[.]golffan[.]us 6820
