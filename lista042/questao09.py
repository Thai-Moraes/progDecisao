'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

num = int(input("Informe a sua idade: "))

resposta = print("Você é menor de idade!") if num < 18 else print("Você é maior de idade!") if num > 18 and num <= 65 else print("Você é idoso KKKKKK")