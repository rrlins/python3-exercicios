# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

jokenpo = ['pedra','papel','tesoura']
computador = choice(jokenpo)
jogador = int(input("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é sua escolha?
>>"""))
jogador = jokenpo[jogador]

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('-='*11)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-='*11)

if jogador == computador:
    print('EMPATE')
elif jogador == 'tesoura' and computador == 'papel':
    print('JOGADOR VENCEU!')
elif jogador == 'papel' and computador == 'pedra':
    print('JOGADOR VENCEU!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('JOGADOR VENCEU!')
elif computador == 'tesoura' and jogador == 'papel':
    print('COMPUTADOR VENCEU!')
elif computador == 'papel' and jogador == 'pedra':
    print('COMPUTADOR VENCEU!')
else:
    print('COMPUTADOR VENCEU!')
