#Crie um prog que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
#A cada pessoa cadastrada, o prog deverá perguntar se o USUÁRIO quer ou não continuar.
#No final, mostre:
# (a) Quantas pessoas tem mais de 18 ANOS.
# (b) Quantos HOMENS foram cadastrados.
# (c) Quantas MULHERES tem menos de 20 ANOS.

M18anos = totalhomens = mulheresmenor20 = 0
while True:
    idade = int(input('digite idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('digite o sexo:')).strip().upper()[0]
    if idade >= 18:
        M18anos += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenor20 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('quer continuar?:')).strip().upper()[0]
    if op == 'N':
        break
print('\nPessoas Maiores de 18anos: ',M18anos)
print('Total de Homens: ',totalhomens)
print('Mulheres com menos de 20anos: ',mulheresmenor20)