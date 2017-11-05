# Desafio 053 - Crie um programa que leia uma frase qualquer e diga se ela é um
#               palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase:\n>> ').lower().strip().replace(' ', '')

# --Código original por: Leandro Montanari (LLM Tutoriais)
#   Adaptado por: Rodrigo Lins
frase = frase.replace('á', 'a')
frase = frase.replace('à', 'a')
frase = frase.replace('ã', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('é', 'e')
frase = frase.replace('ê', 'e')
frase = frase.replace('í', 'i')
frase = frase.replace('ó', 'o')
frase = frase.replace('õ', 'o')
frase = frase.replace('ú', 'u')
frase = frase.replace('ç', 'c')
frase = frase.replace('"', '')
frase = frase.replace("'", "")
frase = frase.replace(',', '')
frase = frase.replace('.', '')
frase = frase.replace('!', '')
frase = frase.replace(';', '')
frase = frase.replace(':', '')
frase = frase.replace('?', '')
frase = frase.replace('-', '')
frase = frase.replace('_', '')
#--------------------------------

print('Essa frase é um palíndromo!'  if frase == frase[::-1] else 'Essa frase não é um palíndromo')
