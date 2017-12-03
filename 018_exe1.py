m = int(input("Digite o número m: "))
n = int(input("Digite o número n: "))

maximo = 0
x_max = 0
y_max = 0

for x in range(m):
	for y in range(n):
			if x*y-x**2+y > maximo:
				maximo = x*y-x**2+y
				x_max = x
				y_max = y

print("O valor máximo é %d, cujo x vale %d e o y vale %d"%(maximo, x_max, y_max))

