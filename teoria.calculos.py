# Pedir 3 notas e armazenar em variáveis 

nota1 = float (input ("Digite a nota 1: "))
nota2 = float (input ("Digite a nota 2: "))
nota3 = float (input ("Digite a nota 3: "))

soma = nota1 + nota2 + nota3
media = soma/3

print ("A media das notas é", media)
if media >= 7:
    print ("Você está aprovado")
else:
    print ("Você foi reprovado")