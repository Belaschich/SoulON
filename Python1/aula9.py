'''
1-Crie uma função que receba dois parâmetros e realize sua soma, subtração, adição e multiplicação.
2-Informe esses resultados através de um print ao usuário dentro da função.
'''

def operacoes(a,b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    
    print("Soma: ", soma)
    print("Subtração: ", sub)
    print("Multiplicação: ", mult)
    print("Divisão: ", div)

operacoes(4,3)