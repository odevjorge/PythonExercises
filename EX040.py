nota1 = float(input("Digite a primiera nota: "))
nota2 = float(input("Digite a segunda nota: "))

m = (nota1 + nota2)/2
if m <= 5.0:
    print(f'Eita, reprovado! MEDIA: {m}')
elif m >= 7.0:
    print(f'Obaaaa, aprovado! MEDIA: {m}')
else:
    print(f'Recuperação, cuidaaaa! MEDIA: {m}')