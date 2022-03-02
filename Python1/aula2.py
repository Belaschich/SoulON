'''
1-Crie três inputs que receba os três dados abaixo:
-Nome do tipo string
-Altura do tipo Float
-CPF do tipo inteiro
2-Exiba através de um único print as três informações para o usuário.
'''

nome = input("Digite seu nome: ")

altura = float(input("Digite sua altura: "))

CPF = int(input("Digite seu CPF: "))

print("Meu nome é {}, tenho {} metros de altura e este é meu CPF:{}". format(nome, altura, CPF))