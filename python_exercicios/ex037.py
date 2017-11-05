# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça
#               para o usuário qual será a base de conversão:
#               1 - Binário
#               2 - Octa
#               3 - Hexadecimal
num = int(input('Digite um número inteiro:\n>>> '))
switch = int(input("""Você quer converte-lo para:
    1-Binário
    2-Octa
    3-Hexadecimal
>> """))

if switch == 1:
    print('Valor em binário: {}'.format(bin(num)))
elif switch == 2:
    print('Valor em octa: {}'.format(oct(num)))
elif switch == 3:
    print('Valor em hexadecimal: {}'.format(hex(num)))
else:
    print('[-] Escolha inválida!')
    print('Digite somente 1,2 ou 3.')
