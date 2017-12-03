"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
as consistências, informando ao usuário nas seguintes situações:
 
    a.  Se o usuário informar o valor de A igual a zero, a equação não é do
    segundo grau e o programa não deve fazer pedir os demais valores,
    sendo encerrado;
 
    b.  Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;
 
    c.  Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;
 
    d.  Se o delta for positivo, a equação possui duas raiz reais; informe-as
    ao usuário;
 
delta = b**2 - 4*a*c
raiz = (-b +ou-(delta**(1/2)))/(2*a)
 
"""

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
	print("A equação não é de segundo grau!")
else:
	delta = b**2 - 4*a*c
	if delta < 0:
		print("As raízes não são reais!")
	elif delta == 0:
		raiz = -b/(2*a)
		print("Só possui a raiz real: %f"%raiz)
	else:
		raiz1 = (-b+delta**(1/2))/(2*a)
		raiz2 = (-b-delta**(1/2))/(2*a)
		print("As raízes são: %f e %f"%(raiz1,raiz2))


	
