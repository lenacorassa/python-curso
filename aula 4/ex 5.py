nota=float(input("coloque uma nota:"))
while nota>10 or nota<0:
    print("nao sabe contar")
    nota = float(input("Digite uma nota: "))

print("Nota válida:", nota)
