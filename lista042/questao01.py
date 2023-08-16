'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Informe um número: "))

resposta = f"O número {num} é acima de 1000" if num > 1000 else f"O número {num} é abaixo de 1000"

print(resposta)