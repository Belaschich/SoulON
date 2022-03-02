'''
Como sugestão de prática, indicamos você a criar um novo script python seguindo as orientações a seguir:
 1-Deve se criar 5 funções diferentes, sendo elas somar, subtrair, dividir, multiplicar e listar.
 2-Deve se criar um MENU com if else sendo que o usuário escolha qual função deve acessar.
 3-Ao ser escolhido a função, o usuário é direcionado a ela e insere os parâmetros que desejam realizar as operações.
 4-As funções matemáticas devem receber os números para realizar a operação, realizar o cálculo e imprimir o resultado para o usuário.
 5-Na função listar, deve-se criar uma lista de vantagens do python e imprimir para o usuário.
'''
def soma (x, y):
    print(x+y)

def Sub (x, y):
    print(x-y)

def div (x, y):
    print(x/y)

def mult (x, y):
    print(x*y)

def listar ():
    print("Vantagens do Python:"
    "1) Programar "
    "2) Fazer Calculos "
    "3) Podemos criar dicionários "
    "4) Utilizado em banco de dados ")

menu = input("Digite qual opção desejada! " 
            "a) Adição " 
            "b) Subtração " 
            "c) Divisão " 
            "d) Multiplicação "
            "e) Vantagens do Python ")

i = 0
while menu != "a" and menu != "b" and menu != "c" and menu != "d" and menu != "e":
    print("Opção não existente, digite novamente!")
    menu = input("Digite qual opção desejada!! "
            "a) Adição " 
            "b) Subtração " 
            "c) Divisão " 
            "d) Multiplicação "
            "e) Vantagens do Python ")
    i =+1
           
if menu =="e":
    listar()    
else:
    x = float(input("Digite um número: "))
    y = float(input("Digite o segundo número: "))

    if menu == "a":
        soma(x,y)
    elif menu =="b":
        Sub(x,y)
    elif menu =="c":
        div(x,y)
    elif menu =="d":
        mult(x,y)