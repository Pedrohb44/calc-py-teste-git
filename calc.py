print("Escolha uma operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite o número da operação desejada (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = num1 + num2
    print("Resultado:", resultado)
elif escolha == '2':
    resultado = num1 - num2
    print("Resultado:", resultado)
elif escolha == '3':
    resultado = num1 * num2
    print("Resultado:", resultado)
elif escolha == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Escolha inválida!")