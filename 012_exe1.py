"""
Dado um número inteiro positivo n,
calcular a soma dos n primeiros números inteiros positivos.
"""

num = int(input("Digite um número: "))
n = num
soma = 0

if num > 0:
    while num != 0:
          soma = soma+num
          num = num - 1;
    print("A soma dos", n, "primeiros números inteiros positivos é", soma)
else:
    print("Não é possivel realizar a soma!")
