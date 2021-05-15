import socket
import threading


PORT = 5000

SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)

FORMAT = "utf-8"

clients, names = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDRESS)


def startServer():
    print("Server is working on " + SERVER)
    server.listen(5)
    
    while True:
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
        
        name = conn.recv(1024).decode(FORMAT)
        
        names.append(name)
        clients.append(conn)
        
        thread = threading.Thread(target = handle, args = (conn, addr))
        
        thread.start()
        

def handle(conn, addr):
    print("handle")
    
    connected = True
    
    while connected:
        message = conn.recv(1024)
        
        print("message: ", message.decode())
    
    



startServer()
    
        