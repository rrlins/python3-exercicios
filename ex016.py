# Desafio 016 - Crie um programa que leia um número Real qualquer pelo teclado
#               e mostre na tela a sua porção Inteira.

from math import ceil, floor, trunc

num = float(input('Digite um número real: '))
print('O valor arredondado para cima: {}'.format(ceil(num)))
print('O valor truncado é: {}'.format(trunc(num)))
print('O valor arredondado para baixo: {}'.format(floor(num)))
