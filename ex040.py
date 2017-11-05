# Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua
#               média, mostrando uma mensagem no final, de acordo com a média
#               atingida:

nota1 = float(input('Digite sua primeira nota:\n>> '))
nota2 = float(input('Digite sua segunda nota:\n>> '))
média = (nota1+nota2)/2

print('Média: {:.2f}'.format(média))

if média < 5:
    print('REPROVADO!')
elif média >= 5 and média < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
