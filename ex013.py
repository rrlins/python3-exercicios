# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
#               com 15% de aumento.

s = float(input('Digite seu salário: '))
print('Seu salário com 15% de aumento fica R${:.2f}.'.format(s + s*15/100))
