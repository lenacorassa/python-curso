def imprimir_numero(numero, quantidade):
    for _ in range(quantidade):
        print(numero)

# Exemplo de uso:
numero_solicitado = int(input("Digite um número: "))
quantidade_solicitada = int(input("Digite a quantidade de vezes que deseja imprimir o número: "))

imprimir_numero(numero_solicitado, quantidade_solicitada)
