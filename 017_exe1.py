candidato1 = candidato2 = candidato3 = 0

num_eleitores = int(input("Digite o número total de eleitores: "))

for i in range(1, num_eleitores+1):
	voto = int(input("Eleitor nº%i digite o número do seu candidato: "%i))
	if voto == 1:
		candidato1 += 1
	elif voto == 2:
		candidato2 += 1
	else:
		candidato3 += 1

print("O candidato 1 teve %i votos" %candidato1)
print("O candidato 2 teve %i votos" %candidato2)
print("O candidato 3 teve %i votos" %candidato3)

if candidato1 > candidato2:
	if candidato1 > candidato3:
		print("O candidato 1 venceu a eleição")

elif candidato2 > candidato3:
	print("O candidato 2 venceu a eleição")

else:
	print("O candidato 3 venceu a eleição")
