umidade = float(input("Digite o percentual de umidade no ar: "))
tempExterna=float(input("Digite o valor da temperatura externa: "))  
if umidade >= 40 and tempExterna <= 20:  
    print("início desumidificação") 
    tempInterna = float(input('Digite o valor da temperatura interna: ')) 
    umidadeInterna=float(input('Digite o percentual da umidade no ar interna: ')) 
    if tempInterna <15:
      print('aquecendo a 100 graus celsius') 
    print('ligando o exaustor')
else:
  print (" iniciando cocção") 
  umidadeInterna=float(input('Digite o percentual da umidade no ar interna: ')) 
  if umidadeInterna>15:
    print("ligando o exaustor")
    tempInterna=float(input('Digite o valor da temperatura interna: '))
  if tempInterna<200: 
      print('aquecendo a 380 graus celsius')