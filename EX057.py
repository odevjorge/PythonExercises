resp = str(input("Digite seu sexo: [M/F] ")).upper().strip()[0]
while resp not in 'MF':
    resp = str(input("Erro, digite novamente: ")).upper().strip()[0]
print(f"Sexo: {resp}")