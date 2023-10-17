import socket
import threading
#Collaboration with Max 
def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Pesan dari {client_address[0]}:{client_address[1]}: {data.decode()}")
        except Exception as e:
            print(f"Kesalahan saat menerima pesan dari {client_address[0]}:{client_address[1]}: {str(e)}")
            break

    client_socket.close()

def start_chat():
    listening_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", listening_port))
    server_socket.listen(5)
    print("Menunggu koneksi dari pengguna lain...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Terhubung dengan {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

def send_message():
    target_ip = input("Masukkan alamat IP tujuan: ")
    target_port = int(input("Masukkan port tujuan: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, target_port))
    print("Terhubung ke tujuan.")

    while True:
        message = input("Masukkan pesan: ")
        client_socket.sendall(message.encode())
        
 
start_chat_thread = threading.Thread(target=start_chat)
start_chat_thread.start()

send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()
