# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros,
#               calcule a sua área e a quantidade de tinta necessária para pintá-la,
#               sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

h = float(input('Digite a altura da parede: '))
b = float(input('Digite a largura da parede: '))
ap = b * h
print('Você irá precisar de {}L para pintar {}m2.'.format(ap/2,ap))
