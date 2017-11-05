# Desafio 023 - Faça um programa que leia um número de 0 a 9999 e ostre na tela cada um dos dígitos separados.

'''
num = inpu('Digite um número de 0 à 9999: ')

if len(num) == 1:
    print('Unidade: {}'.format(num))
elif len(num) == 2:
    print('Unidade: {1}\nDezena: {0}'.format(num[0],num[1]))
elif len(num) == 3:
    print('Unidade: {2}\nDezena: {1}\nCentena: {0}'.format(num[0],num[1],num[2]))
elif len(num) == 4:
    print('Unidade: {3}\nDezena: {2}\nCentena: {1}\nMilhar: {0}'.format(num[0],num[1],num[2],num[3]))
else:
    print('Somente números de 0 a 9999.')
'''

num  = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
