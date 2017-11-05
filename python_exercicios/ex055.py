# Desafio 055 - Faça um programa que leia o peso de cinco pessoas. No final,
#               mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 10**100

for c in range(0,5):
    p = float(input('Digite o peso da {}a pessoa:\n>> '.format(c+1)))
    ultimo = p
    if p > maior:
        maior = p
        continue
    elif p < menor:
        menor = p
        continue
    else:
        continue
print('Maior peso: {}Kg\nMenor peso: {}Kg'.format(maior,menor))
