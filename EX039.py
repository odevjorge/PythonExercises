from datetime import datetime
idade = int(input("Qual ano você nasceu?"))

year = int(f"{datetime.now()}"[:4])

if (year - idade) == 18:
    print(f"Com {(year - idade)} anos, esta na hora de você se alistar!")
elif (year - idade) < 18:
    print(f"Você tem {year - idade} anos e falta {18 - (year - idade)}, ano(s) para voce se alistar!")
else:
    print(f"Você tem {year - idade} anos, já passou do tempo de se alistar em {(year - idade) - 18} anos")