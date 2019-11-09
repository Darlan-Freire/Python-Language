#Crie um prog que calcule o valor a ser pago por um produto.
#Considerando seu preço normal e condição de pagamento:
#Á vista dinheiro/cheque: 10% de desconto
#Á vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print('{:=^35}'.format('LOJAS FREIRE\'s'))
print('[1] Á vista dinheiro:10% de desconto\n[2] Á vista no cartão: 5% de desconto\n', end='')
print('[3] Em até 2x no cartão: preço normal\n[4] 3x ou mais no cartão: 20% de juros')
preço=float(input('Valor total das compras: R$'))
op=int(input('Opção de pagamento:'))

if op==1:
     desc=preço-(preço*0.1)
     print('Total: R${:.2f}'.format(desc))
elif op==2:
    desc=preço-(preço*0.05)
    print('Total: R${:.2f}'.format(desc))
elif op==3:
    print('Preço normal em 2x: R$ {:.2f}'.format(preço/2))
elif op==4:
    x=int(input('Quantas vezes?: '))
    juros=(preço+(preço*0.2))/x
    print('Parcelas em: {}x de R${:.2f}'.format(x,juros))
else:
    print('Opção inválida!')