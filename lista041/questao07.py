'''
 Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Informe um número positivo ou negativo: "))

if num < 0:
    num = num - (num * 2) # multiplicar por (-1) era mais fácil kk

print("O módulo é", num)