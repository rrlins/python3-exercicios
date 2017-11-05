# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: '))
cpc = p - p*5/100
print('O preço com 5% de desconto é {}.'.format(cpc)) 
