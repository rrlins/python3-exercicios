# Desafio 028 - Faça um programa que leia o nome completo de uma pessoa, mostrando
#               em seguida o primeiro e último nome separadamente.

nome = input('Digite seu nome completo: ')
tmp = nome.split()

print('Prazer em conhece-lo {} {}.'.format(tmp[0],tmp[len(tmp)-1]))
