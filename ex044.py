# Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto,
#               considerando o seu preço normal e condição de pagamento:
#               - À vista dinheiro/cheque: 10% de desconto
#               - À vista no cartão: 5% de desconto
#               - Em até 2x no cartão: preço normal
#               - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto:\n>> R$'))
switch = int(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Digite uma opção:
>> """))

if switch == 1:
    desconto = preco - preco*0.10
    print('Você recebeu um desconto de 10%.')
    print('Valor com desconto: R${:.2f}'.format(desconto))

elif switch == 2:
    desconto = preco - preco*0.05
    print('Você recebeu um desconto de 5%.')
    print('Valor com desconto: R%{:.2f}'.format(desconto))

elif switch == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
    print('Valor total: R${:.2f}'.format(preco))

elif switch == 4:
    parcelas = int(input('Digite o número de parcelas:\n>> '))
    if parcelas <=2:
        print('Para parcelar em 2x ou pagar a vista, selecione as outras opções!')
    else:
        juros = preco + preco*0.20
        parcela = juros / parcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas,parcela))
        print('Valor com juros: R${:.2f}'.format(juros))

else:
    print('[ - ] Opção Inválida! Digite apenas 1, 2, 3 ou 4.')
