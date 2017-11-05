frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
am experienced pragrammer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
frase = '  Curso em Vídeo Python  '
print(len(frase.strip()))
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
print(frase[0])
#frase[0] = 'J'
print(frase)
frase1 = frase.replace('Python', 'Android')
print(frase1)
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
divido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
