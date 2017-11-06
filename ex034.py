# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e
#               calcule o valor do seu aumento. Para salários superiores a
#               R$1250,00, calcule um aumento de 10%. Para os inferiores
#               ou iguais, o aumento é de 15%.

print('+'*50)
print('+{:^48}+'.format('SEÇÃO DE AUMENTO'))
print('+'*50)
print()
print('Qual o valor do seu salário??')

sal = float(input(': R$'))

if sal > 1250.00:
    print('Você terá um aumento de 10%!')
    print('Novo salário: R${:.2f}'.format(sal + sal*10/100))
else:
    print('Você terá um aumento de 15%!')
    print('Novo salário: R${:.2f}'.format(sal + sal*15/100))
