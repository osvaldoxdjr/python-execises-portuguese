"""
Dados n e uma seqüência de n números inteiros,
determinar a soma dos números pares.
"""

n = int(input("Digite o tamanho da sequência: "))
cont = 0
soma = 0

while cont < n:
    valor = int(input("Digite o %dº da sequência: " %(cont+1)))
    if valor%2 == 0:
        soma += valor
    cont += 1
print("A soma dos números pares é igual a %d" %soma)
