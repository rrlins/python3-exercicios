# Desafio 015 - Escreva um programa que pergunte a quantidade de Km percorridos
#               por um carro alugado e a quantidade de dias pelos quais ele foi
#               alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
#               por dia e R$0,15 por Km rodado.

kim = float(input('Quantos kilometros foram percorridos? '))
dia = int(input('Quantos dias foi alugado? '))
print('O preço a ser pago será R${:.2f}.'.format(kim*0.15+dia*60))
