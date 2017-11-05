# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a
#               compra de uma casa. Pergunte o valor da casa, o salário do
#               comprador e em quantos anos ele vai pagar.
#               A prestação mensal não pode exceder 30% do salário ou então o
#               empréstimo será negado

valor_casa = float(input('Digite o valor da casa:\n>> R$'))
salário = float(input('Digite seu salário:\n>> R$'))
anos = int(input('Em quantos anos quer pagar?\n>>'))

mensalidade = valor_casa / (anos * 12)
trintap100 = salário * 0.3

print('Valor da mensalidade: R${:.2f}'.format(mensalidade))

if mensalidade <= trintap100:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO RECUSADO!')
