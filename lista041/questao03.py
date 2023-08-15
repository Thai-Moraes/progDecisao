'''
 Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar
'''

num = int(input("Informe um número: "))

if num % 2 == 0:
    print(f'{num} é um número par!')
else:
    print(f'{num} é um número impar!')