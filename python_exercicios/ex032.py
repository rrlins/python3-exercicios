# Desafio 032 - Faça um programa que leia um ano qualquer e mostre se ele é
#               bissexto.

ano = int(input('Digite um ano.: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('{} é bissexto!'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
