#Faça um prog que leia o preço de um produto e mostre seu novo preço, com 5% de desc#

produto=float(input('Digite o valor do produto R$: '))
desc=produto*0.05
print('Valor com 5% de desconto: R$ {:.2f}'.format(produto-desc))




