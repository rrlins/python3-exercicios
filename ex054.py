# Desafio 054 - Crie um programa que leia o ano de nascimento de sete pessoas.
#               No final, mostre quantas ainda não atingiram a maioridade e
#               quantos já são maiores.

from datetime import date

menores = 0
maiores = 0

for c in range(0,7):
    ano_nascimento = int(input('Digite o ano de nascimento da {}o pessoa:\n>> '.format(c+1)))
    idade = date.today().year - ano_nascimento
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print('{} pessoas não atingiram a maioridade.\n{} são maiores de idade.'.format(menores,maiores))
