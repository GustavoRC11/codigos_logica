import os

def cls():

    if os.name == 'nt':
        #Se o sistema é windowos
        os.system("cls")
    else:
        #outros sistemas Linux ou MecOS 
        os.system("clear")   

def somar():

    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    resultado = num1 + num2

    print(resultado)

    
def subtrair():

     
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    resultado = num1 - num2

    print(resultado)
    
def multiplicar():

     
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    resultado = num1 * num2

    print(resultado)
    
def dividir():
     
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    if num2 == 0:
        print("Esse cálculo não pode ser dividido por 0")
    else:
        resultado = num1 / num2

        print(resultado)