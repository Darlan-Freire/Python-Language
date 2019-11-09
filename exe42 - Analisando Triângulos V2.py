#Refaça o EXE35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

x=float(input('comprimento X:'))
y=float(input('comprimento Y:'))
z=float(input('comprimento Z:'))

if x<y+z and y<x+z and z<x+y:
    if x==y==z:
        print('EQUILÁTERO')
    elif x!=y!=z!=x:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('NÃO FORMA TRIÂNGULO')
