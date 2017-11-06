# Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu
#               tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print()
print('O tipo primitivo de {} é {}'.format(n, type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
print()
