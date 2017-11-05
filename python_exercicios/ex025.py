# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem
#               "SILVA" no nome.

nome = input('Digite seu nome completo: ').lower().strip()

print('Seu nome tem Silva.') if 'silva' in nome else print('Seu nome não tem Silva.')
