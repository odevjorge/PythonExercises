valor = float(input("Qual o valor da casa?\n >>> "))
salario = float(input("Qual seu salario?\n >>> "))
anos = int(input("Em quantos anos deseja finalizar o pagamento da casa?\n >>> "))

pm = valor / (anos * 12)
din = salario * (30/100)

if pm > din:
    print(f"STATUS: Negado!\nO valor da parcela mensal é R${pm:.2f} e excede 30% do seu salario que é R${din:.2f}")
else:
    print(f"STATUS: Aprovado!\nO valor da parcela mensal é R${pm:.2f}")
