#Crie um prog que leia o nome de uma cidade e diga e ela começa ou não com o nome 'SANTO'

cidade=str(input('Digite o nome da cidade:')).strip()
print('Nome da cidade, começa com \'SANTO\' ?:',cidade[:5].upper()=='SANTO')
