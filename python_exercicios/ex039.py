# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe,
#               de acordo com a sua idade, se ele ainda vai se alistar ao serviço
#               militar, se é hora de se alistar ou se já passou do tempo do
#               alistamento.
#               Seu programa deve também mostrar o tempo que falta ou que passou
#               do prazo

from datetime import date

ano_nascimento = int(input('Digite o ano em que você nasceu:\n>> '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo = 18 - idade
    ano = ano_atual + tempo
    print('Você tem {0} anos e ainda vai se alistar ao exército.\nÉ para você se alistar em {2} (daqui {1} anos).'.format(idade,tempo,ano))
elif idade > 18:
    tempo = idade - 18
    ano = ano_atual - tempo
    print('Você tem {} anos e já passou do tempo de se alistar ao exército.\nEra para você ter se alistado em {} ({} anos atrás)'.format(idade, ano, tempo))
else:
    print('É hora de se alistar.')
