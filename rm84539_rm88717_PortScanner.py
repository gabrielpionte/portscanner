'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: PortScanner
Alunos
Nome: Fernando de Souza Magaña  - RM: 88717
Nome: Gabriel Pionte Paulino - RM84539
'''
import socket
import threading
from queue import Queue
import time
from datetime import datetime

#Essa parte do código atrela a variável do host com o socket, além de mostrar o inicio do SCAN
print("[ § ] Escanearei todas as portas!!!")
host = input("[ § ] Insira o HOST que deseja realizar o scan: ")
alvo = socket.gethostbyname(host)
print("\n[ § ] Scan sendo feito no HOST: %s IP: %s" % (host, alvo))
print("[ § ]Scan iniciado: %s \n" %(time.strftime("%H:%M:%S")))
dt = datetime.now()
#A linha 25 serve para determinar o tempo das conexões, nesse caso 0.25 segundos.
socket.setdefaulttimeout(0.25)
#A linha 27 serve para evitar modificações ao mesmo tempo, permitindo apenas que uma thread acesse a variavel por vez
print_lock = threading.Lock()
#As próximas linhas são a função de SCAN, ele cria uma conexão SOCKET e verifica as portas abertas.
def scan(pt):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = sckt.connect((alvo, pt))
        with print_lock:
            print("[ § ] Porta aberta: %d" % (pt))
        con.close()
    except:
        pass
#Essa é a função do Thread, ela funciona junto com a biblioteca Queue, essas threads são colocadas em fila, onde a função scan buscará as portas apertas (w)
def tr():
    while True:
        w = q.get()
        scan(w)
        q.task_done()
q = Queue()
#Essas próximas linhas servem para definir a velocidade do SCAN
for x in range(10000):
    t = threading.Thread(target=tr)
    t.daemon = True
    t.start()
#A linha 51 e 52 servem para definir qual é o range de portas que serão escaneadas.
for w in range(1, 65535):
    q.put(w)

q.join()

#E por fim as últimas linhas printa que foi finalizado e quanto tempo demorou o nosso SCAN.
dpt = datetime.now()
ttd = dpt - dt
print("\n[ § ] Scan finalizado as %s " % (time.strftime("%H:%M:%S")))
print("[ § ] Duração do scan: %s " % (ttd))