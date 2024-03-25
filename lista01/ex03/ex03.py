import threading 
import queue 
import random 
import time 

fila = queue.Queue()

def gerar_numeros():
    while True:
        numero = random.randint(1, 100)
        fila.put(numero)
        print(f'Produzido: {numero}')
        time.sleep(1)

def imprimir_numeros():
    while True:
        numero = fila.get()
        print(f'Consumido: {numero}')
        time.sleep(2)

thread_geradora = threading.Thread(target=gerar_numeros)
thread_consumidora = threading.Thread(target=imprimir_numeros)

thread_geradora.start()
thread_consumidora.start()

thread_geradora.join()
thread_consumidora.join() 



