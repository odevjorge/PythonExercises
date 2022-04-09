l = input('Digita uma frase ai:\n >>> ').strip().upper()
print(f'A letra A aparece: {l.count("A")} vezes!')
print(f'Ela aparece primeiro na posição: {(l.find("A")+1)}')
print(f'Ela apareca por umtimo em: {(l.rfind("A")+1)}')
