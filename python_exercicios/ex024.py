# Desafio 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa
#               ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ').lower().strip()

print('A cidade começa com Santo.') if cidade.startswith('santo') else print('A cidade não começa com santo.')
