prd = float(input("Digite o valor do produto: R$"))
formas = int(input(" [1] - Cartão = -5%\n"
                   " [2] - Dinheiro/cheque = -10%\n"
                   " [3] - 2x no cartão: mesmo preço\n"
                   " [4] - 3x ou mais no cartão: +20%\n"
                   "Digite a forma de pagamento: "))

if formas == 1:
    prd -= (prd * 0.05)
elif formas == 2:
    prd -= (prd * 0.1)
elif formas == 3:
    print(f"Parcelado em 2x o valor da parcela fica R${prd/2}")
elif formas == 4:
    pcl = int(input("Quantas parcelas: "))
    prd += (prd * 0.2)
    print(f"Parcelado em {pcl}x o valor da parcela fica R${prd / pcl}")
else:
    print("Opçãp invalida")
print(f'O valor é final é: R${prd:.2f}')
