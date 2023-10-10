def calcular_valor_a_pagar(litros, tipo_combustivel):
    preco_gasolina = 2.50
    preco_alcool = 1.90
    
    if tipo_combustivel == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        valor_total = litros * preco_alcool * (1 - desconto)
    
    elif tipo_combustivel == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        valor_total = litros * preco_gasolina * (1 - desconto)
    
    else:
        print("Tipo de combustível inválido. Use 'A' para álcool ou 'G' para gasolina.")
        return None
    
    return valor_total
  
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")

valor_a_pagar = calcular_valor_a_pagar(litros_vendidos, tipo_combustivel)
if valor_a_pagar is not None:
    print("Valor a ser pago: R$",valor_a_pagar)