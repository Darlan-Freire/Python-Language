#Crie um prog que leia duas notas de um aluno de calcule sua média, mostrando uma mgs no final,
# de acordo com a média atingida.
# - média abaixo de 5: REPROVADO
# - média entre 5 e 6.9: RECUPERAÇÃO
# - média 7 ou superior: APROVADO

nota1=float(input('Digite nota 1:'))
nota2=float(input("Digite nota 2:"))
media=(nota1+nota2)/2
if media <5:
    print('Média = {:.1f} - Aluno REPROVADO'.format(media))
elif media==5 or media<=6.9:
    print("Média = {:.1f} - Aluno em RECUPERAÇÃO".format(media))
else:
    print("Média = {:.1f} - Aluno APROVADO".format(media))


