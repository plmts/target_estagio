"""1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

def fibonacc(max):
  a, b = 0, 1
  sequencia = [a, b]

  while b < max:
    a, b = b, a + b
    sequencia.append(b)
  return sequencia
  
def pertence(n):
  if n < 0:
    return False
  
  sequencia = fibonacc(n)

  if n in sequencia:
    return f"O número {n} pertence à sequencia de Fibonaci!\n"
  else:
    return f"O número {n} não pertence à sequencia de Fibonaci!\n"

n = int(input("\nDesafio 2: \nDigite um número: "))

print(pertence(n))

"""2) Escreva um programa que verifique, em uma string, a existência da letra "a", seja maiúscula ou minúscula, além de informar a 
quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;"""

def contar_letra_a(texto):
    texto = texto.lower()
    quantidade_a = texto.count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) ocorre {quantidade_a} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

string = input("Digite uma string: ")
contar_letra_a(string)


"""3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } 
imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

indice = 12
soma = 0
k = 1

while k < indice:
  k += 1
  soma = soma + k
print(f"\n\nDesafio 1: {soma}\n")


"""4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____"""

def proximo_elemento():
    # a) NÚMEROS ÍMPARES
    sequencia_a = [1, 3, 5, 7]
    proximo_a = sequencia_a[-1] + 2
    print(f"a) Próximo elemento: {proximo_a}")

    # b) PROGRESSÃO GEOMÉTRICA
    sequencia_b = [2, 4, 8, 16, 32, 64]
    proximo_b = sequencia_b[-1] * 2
    print(f"b) Próximo elemento: {proximo_b}")

    # c) QUADRADOS PERFEITOS
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (len(sequencia_c)) ** 2
    print(f"c) Próximo elemento: {proximo_c}")

    # d) QUADRADOS DE NÚMÉROS PARES
    sequencia_d = [4, 16, 36, 64]
    proximo_d = ((len(sequencia_d) + 1) * 2) ** 2
    print(f"d) Próximo elemento: {proximo_d}")

    # e) FIBONACCI
    sequencia_e = [1, 1, 2, 3, 5, 8]
    proximo_e = sequencia_e[-1] + sequencia_e[-2]
    print(f"e) Próximo elemento: {proximo_e}")

    # f) MISTURA DOS ELEMENTOS
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    proximo_f = sequencia_f[-1] + 1 
    print(f"f) Próximo elemento: {proximo_f}")

proximo_elemento()

"""5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?"""

import random
import time

# FUNÇÃO QUE SIMULA AS LAMPADAS
def simular_lampadas():
    # DICIONÁRIO COM AS LÂMPADAS
    return {1: False, 2: False, 3: False}

# LIGAR / DESLIGAR
def ligar_lampada(lampadas, numero):
    lampadas[numero] = True

def desligar_lampada(lampadas, numero):
    lampadas[numero] = False

# FUNÇÃO PARA SIMULAR
def descobrir_lampadas():
    lampadas = simular_lampadas()

    # DEFINE QUAL INTERRUPTOR CONTROLA QUAL LAMPADA
    controle = {1: random.randint(1, 3), 2: random.randint(1, 3), 3: random.randint(1, 3)}
    while len(set(controle.values())) < 3:  
        controle = {1: random.randint(1, 3), 2: random.randint(1, 3), 3: random.randint(1, 3)}

    # SIMULAÇÃO
    print("Ligue o primeiro interruptor (Interruptor 1) por 5 segundos...")
    ligar_lampada(lampadas, controle[1])
    time.sleep(5)

    print("Desligue o primeiro interruptor e ligue o segundo interruptor (Interruptor 2)...")
    desligar_lampada(lampadas, controle[1])
    ligar_lampada(lampadas, controle[2])

    print("Entrando na sala para verificar as lâmpadas...\n")

    # VERIFICA ESTADO DAS LÂMPAAS
    estado_lampadas = {1: "desligada", 2: "desligada", 3: "desligada"}
    for i in range(1, 4):
        if lampadas[i]:
            estado_lampadas[i] = "ligada"

    # IDENTIFICA QUAL O INTERRUPTOR
    for i in range(1, 4):
        if estado_lampadas[i] == "ligada":
            print(f"Lâmpada {i} é controlada pelo Interruptor {controle[i]}.")
        else:
            print(f"Lâmpada {i} é controlada pelo Interruptor {controle[i]} (desligada e fria).")

descobrir_lampadas()

