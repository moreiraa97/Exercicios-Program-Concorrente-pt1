import threading

# Função que será executada por cada thread
def imprimir_numeros(nome):
    for i in range(1, 6):
        print(f'{nome}: {i}')

# Criando as threads
thread1 = threading.Thread(target=imprimir_numeros, args=('Thread 1',))
thread2 = threading.Thread(target=imprimir_numeros, args=('Thread 2',))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

print("Programa finalizado.")
