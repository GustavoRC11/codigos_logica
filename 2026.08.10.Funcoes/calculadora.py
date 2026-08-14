print("=== CALCULADORA ===")



def calculadora():
    while True:
        num1 = float(input("Primeiro número: "))
        operacao = input("Operação (+, -, *, /): ")
        num2 = float(input("Segundo número: "))

        if operacao == "+":
            print("Resultado:", num1 + num2)
        elif operacao == "-":
            print("Resultado:", num1 - num2)
        elif operacao == "*":
            print("Resultado:", num1 * num2)
        elif operacao == "/":
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                print("Resultado:", num1 / num2)
        else:
            print("Operação inválida!")

        continuar = input("Deseja fazer outra conta? (s/n): ")

        if continuar.lower() != "s":
            break

calculadora()