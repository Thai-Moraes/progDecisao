"""
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
"""

num = int(input("Informe um número: "))

if num >= 1 and num <= 10:
    print(f"O número {num} está na faixa de 1 a 10!\n")
else:
    print(f"O número {num} NÃO está na faixa de 1 a 10!\n")

# Operador ternário

print("Operador ternário: ", end="")
resposta = f"O número {num} está na faixa de 1 a 10!" if num >=1 and num <= 10 else f"O número {num} NÃO está na faixa de 1 a 10!"

print(resposta)