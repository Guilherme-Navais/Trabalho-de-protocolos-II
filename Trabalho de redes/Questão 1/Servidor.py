import socket
import threading
import subprocess
import platform

#Laura G. Castro /  Guilherme Navais
#Turma DEV/2N - Desenvolvimento de sistemas


#função TCP
def tcp_server():
    host = 'localhost'
    port = 12345

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print("Servidor TCP esperando por conexões...")
        while True:
            client_socket, client_address = server_socket.accept()
            print("Conexão recebida de:", client_address)
            data = client_socket.recv(1024)
            print('Mensagem recebida do cliente:', data.decode())
            client_socket.sendall("Mensagem recebida com sucesso!".encode()) 
            client_socket.close()
            break
    
    except Exception as e:
        print("Erro:", e)
    
    finally:
        server_socket.close()
        
    return
        
    


#função UDP
def udp_server():
    host = 'localhost'
    port = 12345

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((host, port))
        print("Servidor UDP esperando por mensagens...")
        while True:
            data, client_address = server_socket.recvfrom(1024)
            print("Mensagem recebida do cliente:", data.decode())
            break
    except Exception as e:
        print("Erro:", e)
    finally:
        server_socket.close()
        



#função chat

# Função para lidar com a comunicação do cliente
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print("Mensagem do cliente: ",message.decode())
        except Exception as e:
            print("Erro ao receber mensagem:", e)
            break

# Função principal do servidor de chat
def chat_server():
    host = 'localhost'
    port = 12345

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)  # Permitindo apenas uma conexão de cliente
        print("Servidor de Chat esperando por conexões...")
        client_socket, client_address = server_socket.accept()
        print("Conexão recebida de:", client_address)
        
        # Iniciando a thread para lidar com a comunicação do cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
        
        # Agora o servidor pode enviar mensagens para o cliente
        while True:
            message_to_send = input()
            client_socket.send(message_to_send.encode())
            
    except Exception as e:
        print("Erro:", e)
    finally:
        server_socket.close()



# Função para ICMP (ping)
def handle_icmp():
    ip_address = input("Digite o endereço IP para ping: ")
    print(f"Pinging {ip_address}...")

    # Verifica o sistema operacional
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    try:
        # Monta o comando ping
        result = subprocess.run(['ping', param, '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Comando executado. Código de retorno:", result.returncode)
        if result.returncode == 0:
            # Tenta diferentes codificações
            try:
                response = result.stdout.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    response = result.stdout.decode('latin1')
                except UnicodeDecodeError:
                    response = result.stdout.decode('cp850')
        else:
            response = result.stderr.decode('utf-8')
    except Exception as e:
        response = str(e)
    print("Resultado ICMP:")
    print(response)



# Função para traceroute
def handle_traceroute():
    ip_or_host = input("Digite o IP ou Host para traceroute: ")
    print(f"Tracing route to {ip_or_host}...")

    # Verifica o sistema operacional
    traceroute_cmd = 'tracert' if platform.system().lower() == 'windows' else 'traceroute'

    try:
        result = subprocess.run([traceroute_cmd, ip_or_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Comando executado. Código de retorno:", result.returncode)
        if result.returncode == 0:
            # Tenta diferentes codificações
            try:
                response = result.stdout.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    response = result.stdout.decode('latin1')
                except UnicodeDecodeError:
                    response = result.stdout.decode('cp850')
        else:
            response = result.stderr.decode('utf-8')
    except Exception as e:
        response = str(e)
    print("Resultado Traceroute:")
    print(response)


        

#função que inicia tudo
def menu():
    print("Escolha a funcionalidade do servidor:")
    print("1. TCP")
    print("2. UDP")
    print("3. Chat")
    print("4. ICMP")
    print("5. Traceroute")
    print("6. Encerrar")
    return input("Digite o número da opção desejada: ")


def inicia():
    opcao = menu()

    if opcao == '1':
        tcp_server()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '2':
        udp_server()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '3':
        chat_server()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '4':
        handle_icmp()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '5':
        handle_traceroute()
        print("\n===============================================================================\n")
        inicia()
    elif opcao == '6':
        print("Encerrando o sistema...")
        exit()
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
        print("\n===============================================================================\n")
        inicia()
        

inicia()