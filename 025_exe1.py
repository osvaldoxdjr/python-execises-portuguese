"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
qtde_notas = 4
notas = []
soma = 0

for i in range(1,qtde_notas+1):
	nota = float(input("Digite a %dª nota: "%i))
	soma += nota
	notas.append(nota)
print(notas)
print(soma/qtde_notas)

