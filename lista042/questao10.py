'''
 Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
'''

nome = input("Informe o nome do aluno: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2)/2

print(f"Aluno(a) {nome} está com média {media:.1f}. ", end="")

resposta = print("Ele(a) foi aprovado(a)!") if media >= 7.0 else print("Ele(a) está em Prova Final!") if 3.0 <= media <= 6.9 else print("Ele(a) foi reprovado(a)!")