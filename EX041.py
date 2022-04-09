from datetime import date
ano = int(input("Digite o seu ano de nascimento:\n >>> "))

idade = date.today().year - ano


if idade <= 9:
    print(f"Sua categoria é: MIRIM! IDADE: {idade}")
elif idade <= 14:
    print(f'Sua categoria é: INFANTIL! IDADE: {idade}')
elif idade <= 19:
    print(f'Sua categoria é: JUNIOR! IDADE: {idade}')
elif idade == 20:
    print(f'Sua categoria é: SÊNIOR! IDADE: {idade}')
else:
    print(f'Sua categoria é: MASTER! IDADE: {idade}')
