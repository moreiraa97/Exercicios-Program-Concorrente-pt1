import threading 
import time
import random 

def espera_aleatoria(thread_id):
    espera = random.randint(1, 5)
    print(f'Thread {thread_id} iniciou. Esperando por {espera} segundos...')
    time.sleep(espera)
    print(f'Thread {thread_id} terminou.')

threads = []

for i in range(1, 6):
    thread = threading.Thread(target=espera_aleatoria, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todas as threads terminaram. Programa encerrado.")


