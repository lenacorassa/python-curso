
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

def calcular_operacao(numero1, numero2, operacao):
    if operacao == 1:  # Soma
        resultado = numero1 + numero2
    elif operacao == 2:  # Subtração
        resultado = numero1 - numero2
    elif operacao == 3:  # Divisão
        resultado = numero1 / numero2
    elif operacao == 4:  # Multiplicação
        resultado = numero1 * numero2
    else:
        print("Operação inválida.")
        return None

    return resultado

print("Operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

operacao = int(input("Digite o número da operação desejada: "))

resultado = calcular_operacao(numero1, numero2, operacao)

if resultado is not None:
    print("Resultado: ", resultado)