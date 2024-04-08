import threading 
import time

class Impressora: 
    def __init__(self, nome, tempo_impressao):
        self.nome = nome
        self.tempo_impressao = tempo_impressao 
        self.mutex = threading.Condition()
        self.imprimindo = False 

    def imprimir(self, documento):
        with self.mutex:
            while self.imprimindo:
                self.mutex.wait()
            self.imprimindo = True
            print(f"{self.nome} iniciou a impressao do documento: {documento}")
            time.sleep(self.tempo_impressao)
            print(f"{self.nome} concluiu a impressao do documento: {documento}")
            self.imprimindo = False
            self.mutex.notify_all()


# Funcao para simular a impressao 
def simular_impressao(documento, impressora):
    impressora.imprimir(documento)

# Criando as impressoras
impressora1 = Impressora("Impressora 1", 5)
impressora2 = Impressora("Impressora 2", 2)

# Criando as threads para os documentos
documento1 = threading.Thread(target=simular_impressao, args=("Documento 1", impressora1))
documento2 = threading.Thread(target=simular_impressao, args=("Documento 2", impressora2))
documento3 = threading.Thread(target=simular_impressao, args=("Documento 3", impressora1))
documento4 = threading.Thread(target=simular_impressao, args=("Documento 4", impressora2))

# Iniciando as threads 
documento1.start()
documento2.start()
documento3.start()
documento4.start()

# Aguardando as threads terminarem 
documento1.join()
documento2.join()
documento3.join()
documento4.join()

print("Todos os documentos foram impressos")