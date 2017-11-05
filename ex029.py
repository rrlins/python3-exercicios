# Desafio 029 - Escreva um programa que leia a velocidade de um carro. Se ele
#               ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
#               multado. A multa vai custar R$7,00 por cada Km acima do
#               limite.

speed = int(input('Digite quantos Km/h o cidadão estava.: '))

if speed > 80:
    busted = (speed - 80) * 7
    print('MULTADO!')
    print('Valor da multa:  R${:.2f}'.format(busted))
else:
    print('Dentro da velocidade!')
