#Refaça o EXE9, mostrando a tabuada de um n° que o usuário escolher.
#Utilizando um laço FOR

n=int(input('Tabuada:'))
for c in range(1,10+1):
    print('{} x {} = {}'.format(n,c,n*c))

