import socket
import threading

nickname = input("choose a nickname")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1' , 55555))


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {address}")

        try:
            client.send('NICKNAME'.encode('ascii'))
            nickname = client.recv(1024).decode('utf-8')

            if not nickname:
                client.close()
                continue

            nicknames.append(nickname)
            clients.append(client)

            print(f"nickname of the client is {nickname}")
            broadcast(f"{nickname} joined the chat!".encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

        except Exception as e:
            print(f"error with client {address}: {e}")
            client.close()




def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target = write)
        write_thread.start()