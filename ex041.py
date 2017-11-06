# Desafio 041 - A confederação nacional de natação precisa de um programa que leia
#               o ano de nascimento de um atleta e mostre sua categoria, de acordo
#               com a idade:
#               - Até 9 anos: MIRIM
#               - Até 14 anos: INFANTIL
#               - Até 19 anos: JUNIOR
#               - Até 25 anos: SÊNIOR
#               - Acima: MASTER

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento:\n>> '))
idade = date.today().year - ano_nascimento

print('\nCategoria: ')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
