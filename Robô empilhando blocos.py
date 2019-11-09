#Enunciado do desafio

'''
Nós criamos um robô que move blocos de uma pilha, move eles horizontalmente e depois desce eles até a primeira posição disponível. Existem 10 posições disponíveis para descer os blocos, numeradas de 0 a 9 e cada posição suporta até 15 blocos.
O Robô entende os seguintes comando 'P', 'M' e 'D'
P: Pegar na pilha e mover para posição 0
M: Mover para a próxima posição
D: Descer

O Robô deve ser seguro e respeitar as seguintes regras:
- Sempre existem blocos disponíveis para pegar
- Se o robô já está segurando um bloco ele retorna a posição 0
- Ele não ultrapassa a posição 9, o comando M na posição 9 não faz nada
- Em uma pilha com 15 blocos o comando D não faz nada
- Se o robô nao tiver nenhum bloco o comando D não faz nada
- O Robô ignora qualquer comando que não seja P M D

Escreva uma função que receba uma String como entrada, representando os comandos para o Robô. Como retorno a função devolve uma String representando a quantidade de blocos e cada posição após executar todos os comandos
Entrada = "PMDPMMMDPMDPMMD"
Saida = "0211000000"
'''


# Recebendo a string com os comados para o robô
string = list(input('Digite os comandos para o robô: ').upper())

# Para efeito de teste, está é a string de exemplo no enunciado do desafio
#string = list('PMDPMMMDPMDPMMD')

# Quantidade de blocos em cada pilha, blocos que o robô esteja segurando e a posição atual
amount_of_blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
robot_holding = 0
position = 0

# Função para o robô pegar um bloco da pilha
# E retornar a posição 0
def pick():
    global robot_holding
    global position
    robot_holding = 1
    position = 0

# Função para mover o robô
def move():
    global position
    if position > 8: # Garantia para que não ultrapasse da posição 9
        position = 9
    else:
        position += 1
    
# Função para o robô descer o bloco numa determina posição
def lower():
    global amount_of_blocks
    global robot_holding
    global position
    # Garantia de que o robo esteja realmente segurando um bloco 
    # E que não ultrapasse de 15 blocos empilhados
    if robot_holding > 0 and amount_of_blocks[position] < 16:
        amount_of_blocks[position] += 1
        robot_holding = 0

# Laço para identificar os comandos dados ao robo
for x in string:
    if x == 'P':
        pick()
    elif x == 'M':
        move()
    elif x == 'D':
        lower()

# Checando a quantidade de blocos em cada posição
result = ''.join(str(l) for l in amount_of_blocks)
print(result)

