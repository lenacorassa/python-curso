soma = 0 
contador = 0
aluno = input("Digite o nome do aluno: ") 
while True: 
    entrada = input("Digite a nota do aluno ou S para sair: ") 
    if entrada == 's': 
        break 
    nota = int(entrada) 
    soma = soma + nota 
    contador = contador + 1 
if contador != 0: 
    media = soma / contador 
    print("O aluno ", aluno, "possui a nota: ",media) 