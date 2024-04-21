import threading
import time
import random

class Barbearia:
    def __init__(self, num_cadeiras):
        self.num_cadeiras = num_cadeiras
        self.cadeiras_disponiveis = threading.Semaphore(num_cadeiras)
        self.barbeiros_disponiveis = threading.Semaphore(0)
        self.mutex = threading.Semaphore(1)
        self.clientes_esperando = 0
        self.clientes_atendidos = 0
        self.max_clientes = 10  # Defina o número máximo de clientes a serem atendidos

    def entrar(self):
        if self.cadeiras_disponiveis.acquire(blocking=False):
            self.mutex.acquire()
            self.clientes_esperando += 1
            self.mutex.release()
            print(f"Cliente entrou na barbearia. Cadeiras disponiveis: {self.num_cadeiras - self.clientes_esperando}")
            self.barbeiros_disponiveis.release()
        else:
            print("Barbearia cheia. Cliente saindo.")

    def atender_cliente(self):
        while self.clientes_atendidos < self.max_clientes:
            self.barbeiros_disponiveis.acquire()
            self.mutex.acquire()
            self.clientes_esperando -= 1
            self.clientes_atendidos += 1
            self.mutex.release()
            self.cadeiras_disponiveis.release()
            print("Barbeiro atendendo cliente...")
            time.sleep(random.uniform(0.5, 1.5))
            print("Barbeiro terminou de atender o cliente.")

def cliente(barbearia):
    while barbearia.clientes_atendidos < barbearia.max_clientes:
        time.sleep(random.uniform(0.5, 2))
        barbearia.entrar()

def main():
    num_cadeiras = 5
    num_barbeiros = 2
    barbearia = Barbearia(num_cadeiras)

    threads_barbeiros = []
    for _ in range(num_barbeiros):
        t = threading.Thread(target=barbearia.atender_cliente)
        threads_barbeiros.append(t)
        t.start()

    thread_clientes = threading.Thread(target=cliente, args=(barbearia,))
    thread_clientes.start()

    thread_clientes.join()
    for t in threads_barbeiros:
        t.join()

    print("Fim da simulacao. Todos os clientes foram atendidos.")

if __name__ == "__main__":
    main()
