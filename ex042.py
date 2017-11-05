# Desafio 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
#               mostrar que tipo de triângulo será formado: equilátero, isósceles
#               todos os lados diferentes.

print('\033[34m*\033[m'*50)
print('\033[34m*{:^48}*\033[m'.format(' '))
print('\033[34m*\033[1;34m{:^48}\033[m\033[34m*\033[m'.format('ANALISANDO TRIÂNGULO v2.0'))
print('\033[34m*{:^48}*\033[m'.format(' '))
print('\033[34m*\033[m'*50)

a = float(input('Digite a medida da reta "a": '))
b = float(input('Digite a medida da reta "b": '))
c = float(input('Digite a medida da reta "c": '))

if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triangulo!')
    if a == b == c:
        print('Triangulo equilátero.')
    elif a == b or b == c or a == c:
        print('Triangulo Isósceles.')
    else:
        print('Triangulo Escaleno.')
else:
    print('Não é possível formar um triangulo!')
