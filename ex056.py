# Desafio 056 - Desenvolva um programa que leia o nome, idade e sexo de 4 quatro
#               pessoas. No final do programa, mostre:
#                   - A média de idade do grupo.
#                   - Qual é o nome do homem mais velho.
#                   - Quantas mulheres tem menos de 20 anos.

homem_mais_velho = 0
mm20 = 0
soma_idade = 0

for c in range(0, 4):
    for c in range(1, 200):
        print()
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo(m/f): '))
    soma_idade += idade
    if sexo != 'm' and sexo != 'f':
        print('[-] Digite apenas M ou F para o sexo.')
        break
    if sexo == 'm' and idade > homem_mais_velho:
        nhm_velho = nome
        homem_mais_velho = idade
        continue
    elif sexo == 'f' and idade < 20:
        mm20 += 1
        continue
    else:
        continue

print('A média de idade do grupo é: {:.2f}'.format(soma_idade/4))
print('O nome do homem mais velho é: {}'.format(nhm_velho))
print('Tem {} mulheres com menos de 20 anos.'.format(mm20))
