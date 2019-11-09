#Crie um prog que leia o salário de um funcionário e calcule o valor do seu aumento.
#Para salários maiores que R$1.250,00, calcule um aumento de 10%
#Para salários menores ou iguais, o aumento é de 15%
print('\033[1;35m-=-=\033[m'*8)
sal=float(input('\033[4;34mDigite o salário:\033[m'))
print('\033[1;37m-=-=\033[m'*8)
if sal<=1250:
    novosal=(sal*0.15)+sal
    #print('Novo salário com 15% de aumento: R$',novosal)
else:
    novosal=(sal*0.1)+sal
    #print('Novo salário com 10% de aumento: R$',novosal)
print('\033[1;30mNovo salário:\033[m\033[1;33mR$',novosal)
