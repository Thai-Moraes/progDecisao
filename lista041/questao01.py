'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações
'''

num = float(input("Informe um número: "))

if num > 20:
    print(f"Seu número agora: {num / 2}, a metade de {num}")
else:
    print("Seu número agora:", num)