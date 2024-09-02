# import json

# # # DESAFIO 1
# # """1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# # Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# # Imprimir(SOMA);
# # Ao final do processamento, qual será o valor da variável SOMA?"""

# # indice = 13
# # soma = 0
# # k = 0

# # while k < indice:
# #   k += 1
# #   soma = soma + k
# # print(f"Desafio 1: {soma}\n")


# # #DESAFIO 2
# # """2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# # (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# # ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

# # def fibonacc(max):
# #   a, b = 0, 1
# #   sequencia = [a, b]

# #   while b < max:
# #     a, b = b, a + b
# #     sequencia.append(b)
# #   return sequencia
  
# # def pertence(n):
# #   if n < 0:
# #     return False
  
# #   sequencia = fibonacc(n)

# #   if n in sequencia:
# #     return f"O número {n} pertence à sequencia de Fibonaci!\n"
# #   else:
# #     return f"O número {n} não pertence à sequencia de Fibonaci!\n"

# # n = int(input("\nDesafio 2: \nDigite um número: "))

# # print(pertence(n))


# # #DESAFIO 3
# # """3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# # • O menor valor de faturamento ocorrido em um dia do mês;
# # • O maior valor de faturamento ocorrido em um dia do mês;
# # • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# # IMPORTANTE:
# # a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# # b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

# # ## NÃO ENCONTREI O ARQUIVO JSON QUE O ITEM A) FALTA, POR ISSO CRIEI EU MESMO UM ARQUIVO JSON COM UM FATURAMENTO SEMANAL PARA TESTAR O CÓDIGO

# # with open('desafio3.json', 'r') as file:
# #   dados = json.load(file)

# # def calculo(dados):
# #   faturamento = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

# #   menor = min(faturamento)
# #   maior = max(faturamento)

# #   media = sum(faturamento) / len(faturamento)

# #   acima_media = len([dia for dia in faturamento if dia > media])

# #   return menor, maior, acima_media

# # menor, maior, acima_media = calculo(dados)

# # print(f"\nDesafio 3: \nMenor faturamento diário: {menor}")
# # print(f"Maior faturamento diário: {maior}")
# # print(f"Número de dias com faturamento acima da média: {acima_media}\n")


# """4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
# que cada estado teve dentro do valor total mensal da distribuidora."""

# faturamento_por_estado = {
#     "SP": 67836.43,
#     "RJ": 36678.66,
#     "MG": 29229.88,
#     "ES": 27165.48,
#     "Outros": 19849.53
# }

# total = sum(faturamento_por_estado.values())

# porcentagens = {}
# for estado, valor in faturamento_por_estado.items():
#   porcentagem = (valor / total) * 100
#   porcentagens[estado] = porcentagem
#   print(f"\n{estado}: {porcentagem:.2f}% do faturamento total")

def inverter(lista):
  esquerda = 0
  direita = len(lista) -1

  while esquerda < direita:
    lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
    esquerda += 1
    direita -= 1

  palavra_invertida = ''.join(lista)

  print(f"A palavra intertida fica: {palavra_invertida}")

palavra = str(input("Digite a palavra que você deseja inverter: "))
inverter(list(palavra))