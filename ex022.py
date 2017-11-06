# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#               - O nome com todas as letras maiúsculas e minúsculas.
#               - Quantas letras ao todo (sem considerar espaços).
#               - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
print('Nome com letras maiúsculas: {}.'.format(nome.upper()))
print('Nome com letras minúsculas: {}.'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome)-nome.count(' ')))
spl = nome.split()
print('Total de letras do primeiro nome: {}'.format(len(spl[0])))
