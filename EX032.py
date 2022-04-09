a = input('Digite um ano:\n >>> ')
f = len(a)
if int(a[f-1]) in [2, 4, 6, 8] and int((a[1:5])) % 100 != 0 or int((a[1:5])) % 400 == 0:
    print(f'O ano de {a} é Bissexto!')
else:
    print(f'O ano de {a} não é Bissexto!')