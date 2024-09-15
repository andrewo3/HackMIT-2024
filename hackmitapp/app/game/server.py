import socket, threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',1236))
sock.listen(5)

def handle_conn(client,address):
    buffer = b""
    while True:
        while not b'\n' in buffer:
            data = client.recv(1024)
            if not data:
                print("Close connection with",address)
                client.close()
                return
            buffer+=data
        p,buffer = buffer.split(b"\n",1)
        print(p)
        client.send(b'received '+p+b'\n')
            

try:
    while True:
        (client, address) = sock.accept()
        print("Connected to",address)
        client_conn = threading.Thread(target=handle_conn,args=[client,address])
        client_conn.start()
except Exception:
    sock.close()
