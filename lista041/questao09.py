'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo
'''

num = float(input("Informe um número: "))

if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo")
else:
    print(f"O número {num} é neutro")