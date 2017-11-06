# Desafio 020 - O mesmo professor do desafio 019 quer sortear a ordem de apresentação
#               de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
#               alunos e mostre a ordem sorteada.

from random import shuffle

al = ['nome1','nome2','nome3','nome4']

al[0] = input('Primeiro aluno: ')
al[1] = input('Segundo aluno: ')
al[2] = input('Terceiro aluno: ')
al[3] = input('Quarto aluno: ')

shuffle(al)

print('1- {}'.format(al[0]))
print('2- {}'.format(al[1]))
print('3- {}'.format(al[2]))
print('4- {}'.format(al[3]))

"""
Randomização sem shuffle

ae = randint(0,3)
print('1- {}'.format(al[ae]))
al.remove(al[ae])
ae = randint(0,2)
print('2- {}'.format(al[ae]))
al.remove(al[ae])
ae = randint(0,1)
print('3- {}'.format(al[ae]))
al.remove(al[ae])
ae = al[0]
print('4- {}'.format(ae))
"""
