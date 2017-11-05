# Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os,
#               mostrando na tela uma mensagem:
#               1- O primeiro valor é maior
#               2- O segundo valor é maior
#               3- Não existe valor maior, ambos são iguais

num1 = int(input('Digite um valor inteiro:\n>>>'))
num2 = int(input('Digite outro valor inteiro:\n>>>'))

if num1>num2:
    print('O primeiro valor é maior.')
elif num1<num2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, ambos são iguais.')
