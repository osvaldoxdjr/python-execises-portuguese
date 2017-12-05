"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em metros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.
"""

n = 10

maior_numero = menor_numero = int(input("Digite o número do aluno: "))
maior_altura = menor_altura = float(input("Digite a altura do aluno: "))

for i in range(2,n+1):
	numero = int(input("Digite o número do aluno: ")) 
	altura = float(input("Digite a altura do aluno: "))

	if maior_altura < altura:
		maior_numero = numero
		maior_altura = altura

	if menor_altura > altura:
		menor_numero = numero
		menor_altura = altura

print("O número do aluno mais alto é %d e sua altura é %.2f m"%(maior_numero,maior_altura))
print("O número do aluno mais baixo é %d e sua altura é %.2f m"%(menor_numero,menor_altura)) 
