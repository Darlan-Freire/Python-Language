#Crie um algoritmo que leia um n° e mostre seu dobro, triplo e raiz#

num=int(input("Digite um numero: "))
print("Dobro = {}\nTriplo = {}\nRaiz = {:.2f}".format(num*2,num*3,pow(num,(1/2)))) #ou num**(1/2)
