# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na
#               carteira e mostre quantos dólares ela pode comprar.

n = float(input('Digite quantos reais você tem: R$'))
print('Isso é o equivalente à U${:.2f}'.format(n/3.16))
