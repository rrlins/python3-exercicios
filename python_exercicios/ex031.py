# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem
#               em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
#               para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = float(input('Digite a distancia da viagem.: '))

if distance <= 200:
    distance *= 0.50
    print('Valor da viagem.: R${:.2f}'.format(distance))
else:
    distance *= 0.45
    print('Valor da viagem.: R${:.2f}'.format(distance))
