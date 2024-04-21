import threading

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0
        self.sem = threading.Semaphore(1)

    def incrementar(self):
        while True:
            self.sem.acquire()
            if self.valor >= self.limite:
                self.sem.release()
                break
            self.valor += 1
            print(f"Valor atual do contador: {self.valor}")
            self.sem.release()

def main():
    limite = int(input("Digite o limite para contar: "))
    contador = Contador(limite)
    
    threads = []
    for _ in range(limite):
        t = threading.Thread(target=contador.incrementar)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Contagem finalizada. Valor final do contador: {contador.valor}")

if __name__ == "__main__":
    main()
