'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
'''

num = int(input("Informe um número inteiro de 1 a 7: "))

resposta = print("Domingo") if num == 1 else print("Segunda") if num == 2 else print("Terça") if num == 3 else print("Quarta") if num == 4 else print("Quinta") if num == 5 else print("Sexta") if num == 6 else print("Sábado") if num == 7 else print("Número inválido!")