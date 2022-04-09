# WHILE
num = int(input("Digite um numero: "))

f = num
while num != 1:
    num = num - 1
    f = f * num
print(f)

# FOR
f = 1
num = int(input("Digite um nuemro: "))
for c in range(num, 0, -1):
    f *= c
    print(f" {num}! = {c}" if c == num else c, end="")
    print(' x ' if c != 1 else f" = {f}", end="")
