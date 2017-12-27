"""
Escreva uma função que obtenha a multiplicação de vários números de entrada
"""

def multiplicacao(*nums):
	mult = 1
	for num in nums:
		mult *= num
	return mult
