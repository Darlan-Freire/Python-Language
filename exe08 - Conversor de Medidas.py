#Escreva um prog que leia um valor em metros e o exiba convertidos em centrímetros
#e em milímetros

m=float(input("Digite quantos metros: "))
print("Km = {}\nHm = {}\nDam = {}\nM = {}\nDm = {}\nCm = {}\nMm = {}".format(m/(10**3),m/(10**2),m/10,m,m*10,m*100,m*1000))