'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

resposta = print("{} é maior que {}".format(max(num1, num2), min(num1, num2))) if num1 != num2 else print("Os dois valores são iguais!")

# Sem função max() e min()

resposta = print("{} é maior que {}".format(num1, num2)) if num1 > num2 else print("{} é maior que {}".format(num2, num1)) if num2 > num1 else print("Os dois valores são iguais!")