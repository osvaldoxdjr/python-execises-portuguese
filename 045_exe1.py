"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
 
o   Fatorial de: 5
o   5! =  5 . 4 . 3 . 2 . 1 = 120
 
"""
def fatorial(num):
	if num == 1:
		return 1
	else:
		return fatorial(num-1)*num

def main():
	num = int(input("Fatorial de: "))
	print("%i! ="%num, end = ' ')
	
	for i in range(num,0,-1):
		print("%i"%i, end = ' ')
		if i == 1:
			break
		print(".", end = ' ')
	print("= "+str(fatorial(num)))

main()


