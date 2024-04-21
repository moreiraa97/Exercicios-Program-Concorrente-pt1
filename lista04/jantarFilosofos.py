import threading
import time
import random

class Filosofo:
    def __init__(self, nome, garfo_esquerda, garfo_direita, fim_jantar):
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita
        self.fim_jantar = fim_jantar

    def pensar(self):
        print(f"{self.nome} esta pensando...")
        time.sleep(random.uniform(1, 3))

    def comer(self):
        print(f"{self.nome} esta comendo.")
        time.sleep(random.uniform(1, 3))
        print(f"{self.nome} terminou de comer.")

    def pegar_garfos(self):
        print(f"{self.nome} esta tentando pegar os garfos.")
        garfo1, garfo2 = self.garfo_esquerda, self.garfo_direita
        while not self.fim_jantar.is_set():
            if garfo1.acquire(blocking=False):
                if garfo2.acquire(blocking=False):
                    print(f"{self.nome} pegou os garfos.")
                    return True
                else:
                    garfo1.release()
            time.sleep(random.uniform(0.1, 0.5))
        return False

    def largar_garfos(self):
        print(f"{self.nome} esta largando os garfos.")
        self.garfo_esquerda.release()
        self.garfo_direita.release()

def jantar(filosofos, fim_jantar):
    while not fim_jantar.is_set():
        for filosofo in filosofos:
            filosofo.pensar()
            if fim_jantar.is_set():
                break
            if filosofo.pegar_garfos():
                filosofo.comer()
                filosofo.largar_garfos()

def main():
    num_filosofos = 5
    garfos = [threading.Semaphore(1) for _ in range(num_filosofos)]
    fim_jantar = threading.Event()
    filosofos = [Filosofo(f"Filosofo {i}", garfos[i], garfos[(i + 1) % num_filosofos], fim_jantar) for i in range(num_filosofos)]

    thread_jantar = threading.Thread(target=jantar, args=(filosofos, fim_jantar))
    thread_jantar.start()

    # Espera um tempo antes de encerrar a simulação
    time.sleep(15)

    # Define o evento de fim do jantar
    fim_jantar.set()

    # Para encerrar, interrompe a execução das threads
    thread_jantar.join()

    print("Fim do jantar.")

if __name__ == "__main__":
    main()
