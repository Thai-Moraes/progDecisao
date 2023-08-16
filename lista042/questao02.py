'''
 Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.
'''

num = int(input("Informe um número: "))

resposta = f"O número {num} é abaixo de 1000" if num < 1000 else f"O número {num} está entre 1000 e 5000" if 1000 <= num <= 5000 else f"O número {num} é acima de 5000" if num > 5000 else f'Inválido'
print(resposta)