"""
Escreva um programa que recebe uma lista de números até que seja dada a entrada
-1, e depois imprima todos os números pares da sequência que são pares.
"""

numeros = []

numero = int(input("Digite o número: "))

while numero != -1:
	numeros.append(numero)
	numero = int(input("Digite o número: "))

for num in numeros:
	if num % 2 == 0:
		print(num)
