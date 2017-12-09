"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""
n_numeros = 20
vetor = []
vetor_par = []
vetor_impar = []

for i in range(1,n_numeros+1):
	num = int(input("Digite o numero %i de %i: "%(i,n_numeros)))
	vetor.append(num)

for i in range(n_numeros):
	if vetor[i] % 2 == 0:
		vetor_par.append(vetor[i])
	else:
		vetor_impar.append(vetor[i])

print("O vetor par é:",vetor_par)
print("O vetor ímpar é:",vetor_impar)
