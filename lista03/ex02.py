import threading

# Variável global que será incrementada pelas threads
variavel_global = 0

# Criando um bloqueio para sincronizar o acesso à variável global
lock = threading.Lock()

# Função que será executada por cada thread
def incrementar_variavel():
    global variavel_global
    
    # Incrementando a variável global 100 vezes
    for _ in range(100):
        # Adquirindo o bloqueio antes de acessar a variável global
        lock.acquire()
        variavel_global += 1
        # Liberando o bloqueio após a operação estar completa
        lock.release()

# Criando as threads
thread1 = threading.Thread(target=incrementar_variavel)
thread2 = threading.Thread(target=incrementar_variavel)

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

# Mostrando o valor final da variável global
print("Valor final da variável global:", variavel_global)
