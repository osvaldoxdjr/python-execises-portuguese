n = int(input("Digite um número: "))
cont = 1
soma = 0

while cont < n:
    if n%cont == 0:
        soma += cont
    cont += 1

if soma == n:
    print("O número %d é perfeito"%n)

