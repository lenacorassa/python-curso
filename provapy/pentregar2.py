def verif_posit_neg(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

valor = float(input("Digite um número: "))
resultado = verif_posit_neg(valor)
print("O resultado é:", resultado)
