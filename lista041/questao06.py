'''
 Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido
'''

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

if num1 > num2:
    print(f"O valor da diferença é {(num1 - num2)}")
else:
    print(f"O valor da diferença é {num2 - num1}")

# Daria pra fazer com abs() também, mas como ainda não foi ensinado vai assim mesmo, ia economizar bem mais espaço

# print(f"O valor da diferença é {abs(num1 - num2)}"), nem precisaria de if