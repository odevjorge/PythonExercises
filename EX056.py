midade = 0
c_m = 0
nome_s = 0
for c in range(4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: M ou F: ")[:1].upper()

    midade = midade + idade

    vidade = 0
    if sexo == "M":
        if vidade < idade:
            vidade = idade
            nome_s = nome

    if sexo == "F" and idade < 18:
        c_m += 1

print("Idade media do grupo: {}".format(midade/4))
print("O homem mais velho do grupo tem é: {}".format(nome_s))
print("Tem {} mulheres com menos de 18 anos".format(c_m))