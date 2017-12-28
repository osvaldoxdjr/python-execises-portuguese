"""
Escreva uma função recursiva que retorna a soma de n até zero
"""
def soma(n):
	if n == 1:
		return 1
	else:
		return soma(n-1) + n
