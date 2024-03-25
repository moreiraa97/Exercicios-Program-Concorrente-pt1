import threading

#Variável global
variavel_global = 0

#Bloqueio para sincronização
lock = threading.Lock()

def incrementar():
    global variavel_global
    for _ in range(100):  #Adquire o bloqueio antes de acessar a variável global
        with lock:
            variavel_global += 1


thread1 = threading.Thread(target=incrementar)
thread2 = threading.Thread(target=incrementar)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Valor final da variavel global: ", variavel_global)