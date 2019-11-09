# Faça um prog que calcule a soma entre todos os n° ímpares
# Que são múltiplos de trê
# E que se encontram no intervalo de 1 até 500.
x=0
for c in range(1, 500 + 1,2):
    if c % 3==0:
        x+=c
print(x)