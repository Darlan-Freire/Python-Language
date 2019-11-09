#Faça um prog que mostre a TABUADA de VÁRIOS N°, um de cada vez, para cada valor digitado pelo usuário.
#O prog será INTERROMPIDO quando o n° solicitado for NEGATIVO.
num = 0
while True:
    num = int(input('digite o n° da tabuada, NEGATIVO para sair:'))
    if num < 0:
        break
    else:
        for c in range(1,11):
            print(f'{num} X {c} = {num*c}')
print('fim')