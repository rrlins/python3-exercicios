# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o
#               valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan

ang = int(input('Digite um ângulo: '))
print('Seno: {}'.format(sin(ang)))
print('Cosseno: {}'.format(cos(ang)))
print('Tangente: {}'.format(tan(ang)))
