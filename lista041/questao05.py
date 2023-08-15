'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print(f"Você foi aprovado! Parabéns! Sua nota total foi de {media:.1f}")
else:
    print(f"Infelizmente, você foi reprovado. Sua nota total foi de {media:.1f}")