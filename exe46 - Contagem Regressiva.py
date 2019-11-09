#Faça um prog que mostre ama contagem regressiva de 10 até 0.
#Com uma pausa de 1 segundo entre eles.

from time import sleep

for i in range(10,0,-1):
    print(i)
    sleep(0.5)
print('FELIZ ANO NOVO!!!')