peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = float(f'{peso/(altura * altura):.2f}')

if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f}, você esta Abaixo do Peso!')
elif imc <= 25 or imc <= 30:
    print(f'Seu IMC é {imc:.1f}, você esta no Peso Ideal!')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f}, e você esta com Obesidade')
else:
    print(f'Seu IMC é {imc:.1f}, e você esta com Obesidade Morbida! ')
