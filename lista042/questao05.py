'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

estado = input("Informe um estado brasileiro: ")

resposta = print("O {} está no Sudeste".format(estado)) if estado == "RJ" or estado == "SP" or estado == "MG" or estado == "ES" else print("O {} não está no Sudeste".format(estado))