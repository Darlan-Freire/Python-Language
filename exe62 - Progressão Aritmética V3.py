#Melhore o exe61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O prog encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('digite o termo:'))
razao = int(input('digite a razão:'))
i=0
mais = 10
total = 0
while mais != 0:
    total += mais
    while i < total:
        print(termo, end=' > ')
        termo += razao
        i += 1
    mais = int(input('\nQuantos termos vc quer mostrar mais?'))
print('fim')