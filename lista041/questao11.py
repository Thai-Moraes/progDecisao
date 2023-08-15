'''
 Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

num = int(input("Informe um número de 3 algarismos: "))

if num < 100 or num > 999:
    print("Número inválido! Tente novamente!")
else:
    print(f"O algarismo das centenas de {num} é: {int(num // 100)}")