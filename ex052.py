# Desafio 052 - Faça um programa que leia um número inteiro e diga se ele é ou
#               inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))

for c in range(2,10):
    if c != n and n % c == 0 or n == 1:
        print('Não é primo!')
        break
else:
    print('É primo!')
