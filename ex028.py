# Desafio 028 - Escreva um programa que façao computador "pensar" em um número
#               inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
#               foi o número escolhido pelo computador. O programa deverá
#               escrever na tela se o usuário venceu ou perdeu.

from random import randint

print('='*50)
print('{:^50}'.format('JOGO DA ADVINHAÇÃO v1.0'))
print('='*50)
print()
print("Como Jogar:\nEstou pensando em um número de 1 a 5. Será que você consegue adivinhar qual?")
print('-'*50)

think = randint(1,5)
guess = int(input("Qual número estou pensando?\n:"))

print('VENCEU!' if think == guess else 'PERDEU')
