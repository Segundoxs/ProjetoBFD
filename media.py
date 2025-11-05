nomeAluno = input ("Nome do Aluno")
nota1 = float(input("Primeira Nota "))
nota2 = float(input("Segunda nota"))
media = (nota1 + nota2)/2
print ("A média do aluno", nomeAluno, "é", media)
aprovado = media >=7
if media >=7:
    print ("O aluno está aprovado")
else:
    print ("O aluno está reprovado")