# Desafio 014 - Escreva um programa que converta uma temperatura digitando em
#               graus Celsius e converta para graus Fahrenheit.

gc = float(input('Digite a temperatura em graus celcius: '))
gf = gc*1.8+32
print('{}C equivale à {}F'.format(gc,gf))
