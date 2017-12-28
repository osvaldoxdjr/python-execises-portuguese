"""
Escreva uma função recursiva que imprima de um número x até um y
"""
def imprimeNumero(x,y):
	if x <= y:
		print(x)
		imprimeNumero(x+1,y)

imprimeNumero(2,7)

