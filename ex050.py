# Desafio 050 - Desenvolva um programa que leia seis números inteiros e mostre
#               a soma apenas daqueles que forem pares. Se o valor digitado
#               for impar desconsidere-o.
s = 0
for c in range(0,6):
    n = int(input('Digite o {} número: '.format(c+1)))
    if n % 2 == 0:
        s += n
    else:
        continue
print('A soma dos números pares é: {}'.format(s))
