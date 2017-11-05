# Desafio 035 - Desenvolva um programa que leia o comprimento de três retas e
#               diga ao usuário se elas podem ou não formar um triângulo.

print('\033[34m*\033[m'*50)
print('\033[34m*{:^48}*\033[m'.format(' '))
print('\033[34m*\033[1;34m{:^48}\033[m\033[34m*\033[m'.format('ANALISANDO TRIÂNGULO v1.0'))
print('\033[34m*{:^48}*\033[m'.format(' '))
print('\033[34m*\033[m'*50)

a = float(input('Digite a medida da reta "a": '))
b = float(input('Digite a medida da reta "b": '))
c = float(input('Digite a medida da reta "c": '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triangulo!')
