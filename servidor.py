import _thread
import time
import socket
from functions import *

# Cria o socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pega o nome de host
host = socket.gethostname()
print("host:", host)

# Define a porta a ser usada
port = 9999
print("porta:", port)

# Faz bind
serversocket.bind((host, port))

# Define maximo de conexões simunltâneas no socket (não tenho certeza)
serversocket.listen(5)

print("O servidor esta funcionando\n")

# Função para as threads
def f(serversocket):
    while True:
        data = ""

        # Estabelece conexao
        clientsocket, addr = serversocket.accept()
        print("Conectei com %s" %str(addr))

        # Manda msg para com quem estabeleceu conexao
        msg = "Estou ouvindo" + "\r\n"
        clientsocket.send(msg.encode('ascii'))

        # Fica esperando por pedidos do cliente
        while True:
            msg = clientsocket.recv(1024).decode('ascii')

            # Quando o cliente terminar para de esperar por pedidos do cliente
            if not msg:
                break

            # Atende ao pedido do cliente
            else:
                data += msg

                # 2 '\n's, nesse caso, significa fim de arquivo
                if(msg[len(msg) - 2] == "\n" and msg[len(msg) - 1] == "\n"):

                    # Pega a linha em string, transforma em lista e converte os
                    # valores numéricos para int e float
                    data = linhaPraDados(data)

                    # Calcula o preço total
                    resp = 0
                    for i in data:
                        resp += i[1] * i[2]

                    # Responde o cliente
                    msg = "Numero de itens distintos: " + str(len(data)) + "\nValor total: " + str(resp) + "\r\n"
                    clientsocket.send(msg.encode('ascii'))


        # Encerra a conexao com o cliente
        print("conexao com", addr, "encerrada", "\n")
        clientsocket.close()


# Cria threads para vários usuários acessarem o servidor ao mesmo tempo
try:
    # (function name, (arg1, arg2, argN, ))
    _thread.start_new_thread(f, (serversocket, ))
    _thread.start_new_thread(f, (serversocket, ))
    _thread.start_new_thread(f, (serversocket, ))
    _thread.start_new_thread(f, (serversocket, ))
    _thread.start_new_thread(f, (serversocket, ))
except:
    print ("Erro: Nao foi possivel iniciar a thread")

# Deixa as threads executando
while 1:
    pass
