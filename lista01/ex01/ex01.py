import threading 

def imprimir_numeros(nome):
    for i in range(1, 6):
        print(f'Thread {nome}: {i}')

#Criando duas threads 
thread1 = threading.Thread(target=imprimir_numeros, args=('A',))
thread2 = threading.Thread(target=imprimir_numeros, args=('B',))

#Iniciando as duas threads
thread1.start()
thread2.start()

#Aguardando até que as execuções finalizem
thread1.join()
thread2.join()


