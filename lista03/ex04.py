import threading
import random
import time

# Função que será executada por cada thread
def esperar_tempo(thread_num):
    # Gerando um tempo de espera aleatório entre 1 e 5 segundos
    tempo_espera = random.randint(1, 5)
    print(f"Thread {thread_num} iniciou, esperando {tempo_espera} segundos.")
    time.sleep(tempo_espera)
    print(f"Thread {thread_num} terminou.")

# Lista para armazenar as threads
threads = []

# Criando e iniciando as 5 threads
for i in range(1, 6):
    thread = threading.Thread(target=esperar_tempo, args=(i,))
    threads.append(thread)
    thread.start()

# Aguardando todas as threads terminarem
for thread in threads:
    thread.join()

# Mensagem de conclusão
print("Todas as threads terminaram.")
