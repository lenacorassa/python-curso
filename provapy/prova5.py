slrminimo=1200
salario=int(input("Informe seu salario:"))
if salario<0:
    print("Numero inválido!!")
elif salario>slrminimo:
    print("Salario dentro da legislação:)")
elif salario<slrminimo:
    print("Salario fora da legislação:(")