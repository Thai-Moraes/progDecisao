'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

if num1 % num2 == 0:
    print(f"O número {num2} é divisor de {num1}")
else:
    print(f"O número {num2} NÃO é divisor de {num1}")