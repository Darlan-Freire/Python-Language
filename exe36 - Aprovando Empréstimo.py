#Crie um prog para aprovar um empréstimo bancário para a compra de uma casa.
#O prog vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder mais de 30% do salário
#ou então o empréstimo será negado.

casa=float(input('Qual o valor da casa? R$'))
sal=float(input('Digite o salário: R$'))
anos=int(input('Em quantos anos deseja pagar?:'))
print('{}Calculando{}'.format('-'*10,'-'*10))
desc=sal*0.3
x=anos*12
prest=casa/x

if prest <= desc:
    print('Empréstimo APROVADO!\nValor das prestações:R${:.2f}'.format(prest))
else:
    print('Empréstimo NEGADO... Prestação: R${:.2f}'.format(prest))




