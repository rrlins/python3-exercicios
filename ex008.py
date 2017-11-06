# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite uma medida em metros: '))
print('O valor em centímetros é: {:.1f}'.format(n*100))
print('O valor em milimetros é: {:.1f}'.format(n*1000))
