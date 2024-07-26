import random
import sys
import time

def calcular_pi(numero_de_pontos):
    pontos_dentro_do_circulo = 0

    for _ in range(numero_de_pontos):
        x, y = random.random(), random.random()
        distancia_ao_centro = x**2 + y**2
        if distancia_ao_centro <= 1:
            pontos_dentro_do_circulo += 1

    pi_aproximado = 4 * pontos_dentro_do_circulo / numero_de_pontos
    return pi_aproximado

if __name__ == '__main__':

    numero_de_pontos = int(sys.argv[1])
    start_time = time.time()  # Inicia a medição do tempo
    pi_estimado = calcular_pi(numero_de_pontos)
    end_time = time.time()  # Termina a medição do tempo
    print(f"Aproximação de π com {numero_de_pontos} pontos é: {pi_estimado}")
    print(f"Tempo de execução: {end_time - start_time} segundos")