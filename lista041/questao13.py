'''
 Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

# Jeito mais bonitinho e organizado

num1 = int(input("Informe o valor 1: "))
num2 = int(input("Informe o valor 2: "))
num3 = int(input("Informe o valor 3: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print("Ordem Crescente:", num1, num2, num3)
    else:
        print("Ordem Crescente:", num1, num3, num2)

if num2 < num1 and num2 < num3:
    if num1 < num3:
        print("Ordem Crescente:", num2, num1, num3)
    else:
        print("Ordem Crescente:", num2, num3, num1)

if num3 < num1 and num3 < num2:
    if num1 < num2:
        print("Ordem Crescente:", num3, num1, num2)
    else:
        print("Ordem Crescente:", num3, num2, num1)

# Jeito não encadeado

if (num1 < num2 < num3):
    print(f"Ordem Crescente: {num1, num2, num3}")
if (num1 < num3 < num2):
    print("Ordem Crescente:", num1, num3, num2)
if (num2 < num1 < num3):
    print("Ordem Crescente:", num2, num1, num3)
if (num2 < num3 < num1):
    print("Ordem Crescente:", num2, num3, num1)
if (num3 < num2 < num1):
    print("Ordem Crescente:", num3, num2, num1)
if (num3 < num1 < num2):
    print("Ordem Crescente:", num3, num1, num2)

# Outro jeitinho

menor = min(num1, num2, num3)
maior = max(num1, num2, num3)

print("Ordem Crescente: ", end="")
print(f"{menor}, ", end="")

if (maior + menor) - num2 == num2:
    print(f"{num2}, ", end="")
if (maior + menor) - num1 == num1:
    print(f"{num1}, ", end="")
else:
    print(f"{num3}, ", end="")

print(f"{maior} \n", end="")


