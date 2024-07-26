from threading import Thread

import random
import time
from concurrent.futures import ThreadPoolExecutor


numero_threads = int(input("Digite o número de threads: "))
numero_de_pontos = int(input("Digite o número de pontos: "))
pontos_dentro_circulo_threads = [0] * numero_threads


def calcular_pontos_circulo(numero_de_pontos: int, idx) -> None:
    pontos_dentro_do_circulo = 0
    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distancia_ao_centro = x**2 + y**2
        if distancia_ao_centro <= 1:
            pontos_dentro_do_circulo += 1
    pontos_dentro_circulo_threads[idx] = pontos_dentro_do_circulo


def configurar_threads(numero_de_pontos: int, numero_threads: int) -> list[Thread]:
    threads: list[Thread] = []
    numero_pontos_restantes = numero_de_pontos
    numero_threads_restantes = numero_threads
    pontos_para_cada_thread = round(numero_de_pontos / numero_threads)
    while numero_threads_restantes != 1:
        threads.append(
            Thread(target=calcular_pontos_circulo, args=(pontos_para_cada_thread, numero_threads_restantes - 1))
        )
        numero_pontos_restantes -= pontos_para_cada_thread
        numero_threads_restantes -= 1
    threads.append(Thread(target=calcular_pontos_circulo, args=(numero_pontos_restantes, numero_threads_restantes - 1)))
    return threads


threads = configurar_threads(numero_de_pontos, numero_threads)
start_time = time.time()  # Inicia a medição do tempo

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

pontos_dentro_do_circulo = sum(pontos_dentro_circulo_threads)
pi_aproximado = 4 * pontos_dentro_do_circulo / numero_de_pontos
end_time = time.time()  # Termina a medição do tempo

print(f"Aproximação de π com {numero_de_pontos} pontos é: {pi_aproximado}")
print(f"Tempo de execução: {end_time - start_time} segundos")
