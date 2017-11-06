# Desafio 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma
#               PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o primeiro termo da progresão aritimética: '))
r = int(input('Digite a razão da progresão aritimética: '))
for c in range(0,10):
    print('{}o termo: {}'.format(c+1,n))
    n+=r
