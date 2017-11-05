# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se
#               ele é PAR ou ÍMPAR.

print('\n\n\n\n')

num = float(input('Digite um número.: '))

if num % 2 == 0:
    print('{} é par!'.format(num))
else:
    print('{} é impar!'.format(num))
