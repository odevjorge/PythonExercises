from math import hypot
cop = float(input('Qual o cateto oposto?\n >>> '))
cad = float(input('Qual cateto adjacente?\n >>> '))
print(f'A hipotenusa dos catetos {cop} e {cad} é {hypot(cop, cad):.2f}')
