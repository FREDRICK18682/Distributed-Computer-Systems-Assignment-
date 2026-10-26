import socket #stander network for creating TCP Server
import threading  #to hander multiple users simultaneously with out block others
#creats a custom command that can run from the terminal via manage.py 
from django.core.management.base import BaseCommand

#to track the socket connection of all current connectede users
clients = []

# --- to Craet a command structer  ---
class Command(BaseCommand):
    help = 'Start the ChatRoom Server node'

    def add_arguments(self, parser):
        parser.add_argument('--port',
                            type=int,
                            default=5000,
                            help='port to run the ChatRoom server on')

    # ---- To start the Server ---
      #SOCKET CREATE creates TCP|IP socket
      #SO.RESUABLL ensures that if you stop and restart the srever quickly you wont get an adderss error
    def handle(self, *args, **options):
        port = options['port']
        server = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET,
                          socket.SO.REUSEADDR, 1)
        server.bind(('127.0.0.1', port))
        server.listen()

        #To show thata the server has started successfully 
        self.stdout.write(
            self.style.SUCCESS(f'[SERVER STARTED ] listening on port {port}!!!')
        )
    # --- To accept the connection loop ---
     # the server continusly listrens for new clinets when a clint connection is add to the socket to the client listen and swaps a new background thread to hander the specific 
        while True:
            client_socket, client_address = server.accept()
            client.append(client_socket)
            thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, client_address)
            )
            thread.start()

        

    # --- to handel client ---
    #handel communcation 
    def handle_client(self, client_socket, client_address):

    
        print(f'[NEW CONNECTION ] {client_address} connected')
        # creat a loop
        while True:
            try:
                message = client_socket.recv(1024)
                #to check if user has disconnected 
                if not message:
                    #exist the loop
                    break
                # to sen the message to other connected users 
                self.broadcast(message, client_socket)
            #to handel connection error
            except:
                break
            #o close the user socket
            client=socket.close()
            #to remove the user from the list
            if client_socket in client:
                client.remove(client_socket)

    # --- to semd mssages from one user to all other connceted users 
    def broadcast(self, message, sender_socket):
        for client in clients:
            #excluders the sender
            if client != sender_socket:
                try:
                  client.send(message)
                except OSError:
                   clients.remove(client)
                   client.close()
                  