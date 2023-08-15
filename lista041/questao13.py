'''
 Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

# Essa não sei se todas deram certas, mas a maioria foi

num1 = int(input("Informe o valor 1: "))
num2 = int(input("Informe o valor 2: "))
num3 = int(input("Informe o valor 3: "))

if num1 < num2 and num1 < num3:
    print(f"{num1} ", end="")
    if num2 < num3:
        print(num2, num3)
    else:
        print(num3, num2)

if num2 < num1 and num2 < num3:
    print(f"{num2} ", end="")
    if num1 < num3:
        print(num1, num3)
    else:
        print(num3, num1)

if num3 < num1 and num3 < num2:
    print(f"{num3} ", end="")
    if num1 < num2:
        print(num1, num2)
    else:
        print(num2, num1)
