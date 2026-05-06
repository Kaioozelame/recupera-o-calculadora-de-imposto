valor=float(input("Digite o valor do produto importado:"))
if valor >50:
    imposto=valor*0.60
else:
    imposto=valor *0.17

    valor_final= valor + imposto

    print(f"Valor do produto:$ {valor:.2f}")
    print(f"Imposto aplicado:$ {imposto:.2f}")
    print(f"Valor final com imposto:${valor_final:.2f}")