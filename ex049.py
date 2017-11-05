# Desafio 049 - Refaça o DESAFIO 009, mostrando a tabuada de um número que o
#               usuário escolher, só que agora com o laço for.

n = int(input('Qual número deseja ver a tabuada?\n>> '))
for c in range(1,11):
    print('{} x {} = {}'.format(n,c,n*c))
