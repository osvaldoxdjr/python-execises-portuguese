"""
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10.
"""

elementos = []

elemento = int(input("Digite o elemento: "))

while elemento != -1:
	elementos.append(elemento)
	elemento = int(input("Digite o elemento: "))

for numero in elementos:
	if numero > 10:
		print(numero)
