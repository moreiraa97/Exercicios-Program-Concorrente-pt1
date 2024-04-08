import random 
import threading 
from datetime import datetime


numero_sorteado = 0
numero_encontrado = False 
numero_maximo = 1000

def gerarNumeroAleatorio():
    global numero_sorteado 
    numero_sorteado = random.randint(1, numero_maximo)
    print("Numero sorteado: ", numero_sorteado)

def descobrirNumeroGerado(controle):
    global numero_sorteado, numero_encontrado 
    chute_inicial = int(numero_maximo/2) 
    chute = chute_inicial 
    if(controle):
        chute = chute_inicial+1

    while not numero_encontrado:

        print(threading.current_thread().name, " ", chute)

        if chute < numero_sorteado:
            chute += 2
        elif chute > numero_sorteado:
            chute -= 2
        else:
            print("Numero econtrado pela Thread: ", threading.current_thread().name)
            numero_encontrado = True
            break 

def main():
    gerarNumeroAleatorio()

    thread1 = threading.Thread(target=descobrirNumeroGerado, name="Thread 1", args=(True,))
    thread2 = threading.Thread(target=descobrirNumeroGerado, name="Thread 2", args=(False,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


inicio = datetime.now()

main()

print(datetime.now() - inicio)












