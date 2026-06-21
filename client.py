import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Disconnected from server")
            client.close()
            break

def write():
    while True:
        message = input("")
        client.send(f'{nickname}: {message}'.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.daemon = True
write_thread.start()

receive_thread.join()