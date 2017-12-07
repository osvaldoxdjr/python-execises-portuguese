"""
Dados x e E reais, E > 0, calcular uma aproximação para sen x através da
seguinte série infinita
 
sen x = x/(1!) - (x**3)/(3!) + (x**5)/(5!) -...+((-1)**k)*(x**(2*k+1))/((2*k+1)!)
     
      incluindo todos os termos até que
 
modulo(x**(2*k+1))/((2*k+1)!) < E
 
     Compare com os resultados de sua calculadora! 
"""
from math import fabs, factorial, sin

x = float(input("Digite o número real x: "))
E = float(input("Digite o número real E: "))

while x < 0 or E < 0:
	print("Digite x e E maiores que 0")
	x = float(input("Digite o número real x: "))
	E = float(input("Digite o número real E: "))

sen_x = x
term = x
i = 1

while fabs(term) > E:
	term = ((-1)**i)*(x**(2*i+1))/(factorial(2*i+1))
	sen_x += term
	i += 1

print("O valor da calculadora é: %f"%sin(x))
print("O valor aproximado é: %f"%sen_x)
	
