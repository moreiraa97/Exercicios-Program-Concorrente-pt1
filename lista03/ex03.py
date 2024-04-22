import threading
import queue
import random
import time

# Fila para armazenar os números gerados aleatoriamente
fila = queue.Queue()

# Bloqueio para sincronizar o acesso à fila
lock = threading.Lock()

# Função que gera números aleatórios e os coloca na fila
def gerar_numeros():
    while True:
        # Gerando um número aleatório entre 1 e 100
        numero = random.randint(1, 100)
        
        # Adquirindo o bloqueio antes de manipular a fila
        lock.acquire()
        
        # Colocando o número na fila
        fila.put(numero)
        
        # Liberando o bloqueio após a operação estar completa
        lock.release()
        
        # Aguardando um intervalo antes de gerar o próximo número
        time.sleep(1)

# Função que retira os números da fila e os imprime na tela
def imprimir_numeros():
    while True:
        # Adquirindo o bloqueio antes de manipular a fila
        lock.acquire()
        
        # Verificando se a fila não está vazia
        if not fila.empty():
            # Retirando o número da fila
            numero = fila.get()
            print("Número retirado da fila:", numero)
        
        # Liberando o bloqueio após a operação estar completa
        lock.release()
        
        # Aguardando um intervalo antes de verificar a fila novamente
        time.sleep(2)

# Criando e iniciando as threads
thread_gerar = threading.Thread(target=gerar_numeros)
thread_imprimir = threading.Thread(target=imprimir_numeros)

thread_gerar.start()
thread_imprimir.start()

# Aguardando as threads terminarem (isso nunca acontecerá porque as threads são infinitas)
thread_gerar.join()
thread_imprimir.join()
