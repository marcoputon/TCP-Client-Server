import socket
import time
import sys
from functions import *


# Pega valores passados pela linha de comando
try:
    ipserver = sys.argv[1]
    porta = int(sys.argv[2])
    pedido = sys.argv[3]

# Se não conseguir eh porque faltaram parâmetros
except:
    print("Erro: Faltaram parametros.")
    raise SystemExit

# Pedido a ser enviado para o servidor
pedido = openFile(pedido)


# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pega o host name
host = socket.gethostname()

# Define a porta a ser usada
port = porta

# Tenta conectar com o servidor
try:
    s.connect((ipserver, port))

# Se não conseguir, encerra o programa
except:
    print("Nao foi possivel conectar ao servidor")
    raise SystemExit

msg = s.recv(1024)
print ("Recebi do servidor:", msg.decode('ascii'))

# Manda o pedido
for i in pedido:
    time.sleep(1)
    msg = i + "\n"
    s.send(msg.encode('ascii'))

    # Tempo para "separar" o que o servidor vai receber
    #time.sleep(0.1)

msg = s.recv(1024)
print("Recebi do servidor:\n" + msg.decode('ascii'))


s.close()
print("Conexao com o servidor encerrada")
