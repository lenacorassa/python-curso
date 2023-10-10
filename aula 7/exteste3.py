nota1 = float(input("Nota 1 :"))
nota2 = float(input("Nota 2 :"))
nota3 = float(input("Nota 3 :"))
nota1 *= 1
nota2 *= 1.5
nota3 *= 2
soma = nota1 + nota2 + nota3
# soma = nota1 *1 + nota2 *1.5 + nota3 * 2

media = soma /4.5
print(media)
"""if media >= 9:
   print("SS")
elif media < 9 and media >= 7:
   print("MS")
elif media < 7 and media >= 5:
   print("MM")
elif media < 5 and media >= 2:
   print("MI")
elif media < 2 and media > 0:
print("II")
else:
   print("SR")"""
# SR - 0
# II - < 2
# MI - < 5
# MM - < 7
# MS - < 9
# SS - >=9
if media == 0  :
   print("SR")
elif media <0:
   exit("numero negativo nao es valido")
elif media < 2 :
   print("II")
elif media < 5 :
   print("MI")
elif media < 7:
   print('MM')
elif media < 9:
   print("MS")
elif media >= 9 and media <=10:
   print("SS")

