"""
Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número
"""

num1 = int(input("Informe valor 1: "))
num2 = int(input("Informe valor 2: "))
num3 = int(input("Informe valor 3: "))
num4 = int(input("Informe valor 4: "))
num5 = int(input("Informe valor 5: "))

# Jeito rápido (e fácil) de fazer

print(f"\nO maior valor é: {max(num1, num2, num3, num4, num5)}\nO menor valor é: {min(num1, num2, num3, num4, num5)}")

# Jeito demorado (e que não tenho 100% de certeza se está funcionando)

menor = num1
maior = num1

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
if menor > num3:
    menor = num3
if menor > num4:
    menor = num4
if menor > num5:
    menor = num5

if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
if maior < num3:
    maior = num3
if maior < num4:
    maior = num4
if maior < num5:
    maior = num5

print(f"\nO maior valor é: {maior}\nO menor valor é: {menor}")

