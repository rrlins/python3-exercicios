# Desafio 048 - Faça um programa que calcule a soma entre todos os números ímpares
#               ímpares que são múltiplos de três e que se encontram no intervalo
#               de 1 até 500.
s = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 == 1:
        print(c)
        s+=c
    else:
        continue
print('\n\nSoma: {}'.format(s))
