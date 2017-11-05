# Desafio 043 - Desenvolva uma lógiva que leio o peso e a altura de uma pessoa,
#               calcule seu IMC e mostre seu status, de acordo com a tabela
#               abaixo:
#               - Abaixo de 18.5: Abaixo do peso
#               - Entre 18.5 e 25: Peso ideal
#               - 25 até 30: Sobrepeso
#               - 30 até 40: Obesidade
#               - Acima de 40: Obesidade mórbida

p = float(input('Digite seu peso (Kg):\n>> '))
h = float(input('Digite sua altura (m):\n>> '))
imc = p / h**2

print('Seu IMC é: {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc < 25:
    print('Peso ideal!')
elif imc < 30:
    print('Sobrepeso!')
elif imc < 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida!')
