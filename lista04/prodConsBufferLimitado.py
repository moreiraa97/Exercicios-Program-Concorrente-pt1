import threading
import time
import random

class Buffer:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.buffer = []
        self.mutex = threading.Semaphore(1)
        self.pode_produzir = threading.Semaphore(capacidade)
        self.pode_consumir = threading.Semaphore(0)
        self.itens_produzidos = 0
        self.itens_consumidos = 0

    def produzir(self, item):
        self.pode_produzir.acquire()
        self.mutex.acquire()
        self.buffer.append(item)
        self.itens_produzidos += 1
        print(f"Item produzido: {item}")
        print(f"Buffer: {self.buffer}")
        self.mutex.release()
        self.pode_consumir.release()

    def consumir(self):
        self.pode_consumir.acquire()
        self.mutex.acquire()
        item = self.buffer.pop(0)
        self.itens_consumidos += 1
        print(f"Item consumido: {item}")
        print(f"Buffer: {self.buffer}")
        self.mutex.release()
        self.pode_produzir.release()

def produtor(buffer, max_itens):
    for _ in range(max_itens):
        item = random.randint(1, 100)
        buffer.produzir(item)
        time.sleep(random.uniform(0.1, 0.5))

def consumidor(buffer, max_itens):
    while buffer.itens_consumidos < max_itens:
        buffer.consumir()
        time.sleep(random.uniform(0.1, 0.5))

def main():
    capacidade_buffer = 5
    max_itens = 20  # Defina o número máximo de itens a serem produzidos e consumidos
    buffer = Buffer(capacidade_buffer)

    thread_produtor = threading.Thread(target=produtor, args=(buffer, max_itens))
    thread_consumidor = threading.Thread(target=consumidor, args=(buffer, max_itens))

    thread_produtor.start()
    thread_consumidor.start()

    thread_produtor.join()
    thread_consumidor.join()

    print("Fim da simulacao.")

if __name__ == "__main__":
    main()
