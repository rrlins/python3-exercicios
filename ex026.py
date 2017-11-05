# Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre quantas
#               vezes aparece a letra "A", em que posição ela aparece a primeira
#               vez e em que posição ea aparece a última vez.

frase = input('Digite uma frase: ').lower().strip()

print('Aparecem {} veze(s) a letra "A".'.format(frase.count('a')))
print('A primeira aparece na posição: {}.'.format(frase.find('a')))
print('A última aparece na posição: {}.'.format(frase.rfind('a')))
