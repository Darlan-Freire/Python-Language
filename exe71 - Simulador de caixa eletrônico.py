#Faça um prog que simule o funcionamento de um CAIXA ELETRÔNICO.
#No início, pergunte ao usuário qual será o VALOR A SER SACADO(n° inteiro)
#e o prog vai informar quantas CÉDULAS de cada valor serão entregues.
#OBS.: Considere que o caixa possui cédulas de R$100, 50, 20, 10, 2 e 1.

valor = int(input('Qual o valor a ser sacado?:'))
total = valor
cédula = 100
total_cédula = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédula += 1
    else:
        if total_cédula > 0:
            print('Total de cédulas de {} = {}'.format(cédula,total_cédula))
        total_cédula = 0
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 2
        elif cédula == 2:
            cédula = 1
        elif total == 0:
            break
print('VOLTE SEMPRE!')