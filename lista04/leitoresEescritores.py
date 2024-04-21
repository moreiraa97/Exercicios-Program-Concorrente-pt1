import threading
import time
import random

class LeitorEscritor:
    def __init__(self):
        self.recurso = 0
        self.mutex_leitura = threading.Semaphore(1)
        self.mutex_escrita = threading.Semaphore(1)
        self.leitores = 0
        self.escritores = 0
        self.max_leituras = 10  # Defina o número máximo de leituras
        self.max_escritas = 3  # Defina o número máximo de escritas

    def ler_recurso(self, leitor_id):
        leituras_feitas = 0
        while leituras_feitas < self.max_leituras:
            time.sleep(random.uniform(0.5, 1.5))
            self.mutex_leitura.acquire()
            self.leitores += 1
            if self.leitores == 1:
                self.mutex_escrita.acquire()
            self.mutex_leitura.release()

            print(f"Leitor {leitor_id} esta lendo o recurso: {self.recurso}")
            leituras_feitas += 1

            self.mutex_leitura.acquire()
            self.leitores -= 1
            if self.leitores == 0:
                self.mutex_escrita.release()
            self.mutex_leitura.release()

    def escrever_recurso(self, escritor_id):
        escritas_feitas = 0
        while escritas_feitas < self.max_escritas:
            time.sleep(random.uniform(1, 2))
            self.mutex_escrita.acquire()
            novo_valor = random.randint(1, 100)
            print(f"Escritor {escritor_id} esta escrevendo o recurso com valor: {novo_valor}")
            self.recurso = novo_valor
            escritas_feitas += 1
            self.mutex_escrita.release()

def main():
    num_leitores = 5
    num_escritores = 2

    leitor_escritor = LeitorEscritor()

    threads_leitores = []
    for i in range(num_leitores):
        t = threading.Thread(target=leitor_escritor.ler_recurso, args=(i,))
        threads_leitores.append(t)
        t.start()

    threads_escritores = []
    for i in range(num_escritores):
        t = threading.Thread(target=leitor_escritor.escrever_recurso, args=(i,))
        threads_escritores.append(t)
        t.start()

    # Espera até que todas as leituras e escritas sejam concluídas
    for t in threads_leitores:
        t.join()

    for t in threads_escritores:
        t.join()

    print("Fim da simulacao.")

if __name__ == "__main__":
    main()
