hora = int(input("Que horas são ? "))

if 0<=hora and 6>hora:
  print("Agora são:", hora, "hora(s). Boa Madrugada!!")
elif 6<=hora and 12>hora:
  print("Agora são", hora, "hora(s). Bom Dia!!")
elif 12<=hora and 18>hora:
  print("Agora são", hora, "hora(s). Boa Tarde!!")
elif 18<=hora and 24>hora:
  print("Agora são", hora, "hora(s). Boa Noite!!")
else:
  print("hora inválida:(")
