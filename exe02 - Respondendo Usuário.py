#Faça um prog que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

cores={'vermelho':'\033[1;31;40m','limpa':'\033[m' }
nome=str(input('Qual seu nome?')).strip()
print('Ola {}{}{}, Seja bem-vindo'.format(cores['vermelho'], nome,cores['limpa']))
