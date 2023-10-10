numeros = []
numero = int(input("Digite um número (ou -1 para sair): "))

while numero != -1:
    numeros.append(numero)
    numero = int(input("Digite um número (ou -1 para sair): "))

if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print("O maior número é:", maior)
    print("O menor número é:", menor)
else:
    print("Nenhum número foi fornecido.")