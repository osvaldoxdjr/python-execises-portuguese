"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
n = 4 --> 1, 3, 5, 7
n = 3 --> 1, 3, 5
n = 7 --> 1, 3, 5, 7, 9, 11, 13
"""

n = int(input("Digite um número: "))
n = n-1
imp = 1
print(imp)

while n != 0:
    imp = imp + 2
    print(imp)
    n = n-1
