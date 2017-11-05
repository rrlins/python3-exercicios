# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do
#               cateto adjacente de um triângulo retângulo. Calcule e mostre
#               o comprimento da hipotenusa.

from math import sqrt

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = sqrt(ca**2+co**2)
print('A hipotenusa é: {:.3f}'.format(h))
