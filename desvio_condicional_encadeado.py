'''
Crie um programa que pergunte um número ao usuário.
Em seguida o programa deve informar se o número inserido
está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

num = int(input("Digite um número:"))

if ( num < 100 ):
    print(num, " está abaixo de 100.")
else:
    if( num <= 200 ):
        print(num, " está entre 100 e 200.")
    else:
        print(num, " está acima de 200.")