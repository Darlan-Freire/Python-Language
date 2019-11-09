#Faça um prog que leia NOME, IDADE e SEXO de 4 pessoas.
#No final, mostre:
#>>> A média de idade do grupo.
#>>> Qual é o nome do homem mais velho.
#>>> Quantas mulheres têm menos de 20 anos.
nome_mais_velho=''
id_mais_velho=0
total_mulheres=0
id=0
for c in range (0,4):
    print('==={}° Pessoa==='.format(c+1))
    nome=str(input('Digite seu nome:')).strip()
    idade=int(input('Digite sua idade:'))
    sexo=str(input('Sexo [M/F]:')).upper().strip()
    id+=idade

    if sexo in 'Mm' and idade > id_mais_velho:
        id_mais_velho=idade
        nome_mais_velho=nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres+=1


media=id/4
print('A média de idade do grupo é: {}'.format(media))
print('A idade do homem mais velho é: {} anos, e se chama: {}'.format(id_mais_velho,nome_mais_velho))
print('Total de mulheres com menos de 20 anos: ',total_mulheres)