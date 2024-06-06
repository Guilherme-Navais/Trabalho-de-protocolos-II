import socket
import threading

#Laura G. Castro /  Guilherme Navais
#Turma DEV/2N - Desenvolvimento de sistemas


#função do protocolo TCP
def tcp_client():
    host = 'localhost'
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        message = input("Digite a mensagem para enviar ao servidor: ")
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print('Mensagem recebida do servidor:', data.decode())
    except Exception as e:
        print("Erro:", e)
    finally:
        client_socket.close()
        
   

#função do protocolo UDP
def udp_client():
    host = 'localhost'
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = input("Digite a mensagem para enviar ao servidor: ")
        client_socket.sendto(message.encode(), (host, port))

    except Exception as e:
        print("Erro:", e)
    finally:
        client_socket.close()
        
       

#função chat
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print("Mensagem do servidor: ",data.decode())
        except Exception as e:
            print("Erro ao receber mensagem:", e)
            break


def chat_client():
    host = 'localhost'
    port = 12345

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
        while True:
            message = input()
            if message.lower() == 'sair':
                break
            client_socket.sendall(message.encode())
    except Exception as e:
        print("Erro:", e)
    finally:
        client_socket.close()
        

#Aqui é a função menu que inicia tudo
def menu():
    print("Escolha o protocolo de comunicação:")
    print("1. TCP")
    print("2. UDP")
    print("3. Chat")
    print("4. Encerrar")
    return input("Digite o número da opção desejada: ")

def inicia():
    opcao = menu()

    if opcao == '1':
        tcp_client()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '2':
        udp_client()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '3':
        chat_client()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '4':
        print("Encerrando o sistema...")
        exit()
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
        print("\n===============================================================================\n")
        inicia()
        
inicia()
