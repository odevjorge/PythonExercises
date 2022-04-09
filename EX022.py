nome = input('Oieee, me diz teu nome:\n >>> ').strip()
p = nome.split()
print(f'Seu nome em MAIUSCULO é: {nome.upper()}\n'
      f'Seu nome em MENUSCULO é: {nome.lower()}\n'
      f"Seu nome tem {len(nome.replace(' ', ''))} letras!\n"
      f"Seu primeiro nome tem {len(p[0])} letras!\n")
