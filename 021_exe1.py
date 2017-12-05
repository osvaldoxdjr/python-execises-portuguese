"""
Dados x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/((2k)!)
 
Compare com os resultados de sua calculadora!
"""

x = float(input("Digite um número real: "))
n = int(input("Digite um número natural: "))

cos_x = fact = 1

for i in range(1,n+1):
	for j in range(1,i*2+1):
		fact *= j
	if i%2 == 0:
		cos_x += (x**(i*2))/fact
	else:
		cos_x -= (x**(i*2))/fact	
	fact = 1

print("O valor aproximado de cos x é: %f"%cos_x)
