'''
Crie um programa que pergunte a idade de uma pessoa.
Em seguida o programa deve informar se a pessoa é menor de idade
ou se é maior de idade.
'''

idade = int(input("Informe a sua idade: "))

if (idade < 18):
    print("Você é menor de idade!")
else:
    print("Você é maior de idade!")