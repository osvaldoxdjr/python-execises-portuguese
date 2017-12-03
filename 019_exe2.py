"""
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.
 
Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
"""

i = int(input("Digite i: "))
j = int(input("Digite j: "))

n = 1

while n < i or n < j:
	if i % n == 0 and j % n == 0:
		print (n)
	n += 1 
