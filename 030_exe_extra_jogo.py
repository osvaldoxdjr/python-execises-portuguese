from random import *

vida = 10
sp = 100

vida_ini = 10
vidas_ini = []

dano_ini = []
dano_ini_tot = 0

vec_ale = []
derr = []

cont = 0



inimigos = int(input("Digite o número de inimigos: "))
for i in range(inimigos):
	vidas_ini.append(vida_ini)

while vida > 0 and cont != inimigos:
	cont = 0

	print("Vida: %i"%vida)
	print("SP: %i"%sp)
	acao = int(input("Deseja atacar (1) ou deseja curar (2): "))
	
	if acao == 1:
			dano_joga = randint(10,15)	
	
			
			for i in range(0,inimigos):
				vec_ale.append(i)

			for i in derr:
				vec_ale.remove(i)

			escolha = choice(vec_ale)

			vec_ale = []


			vidas_ini[escolha] -= dano_joga
			print("Causou %i de dano ao inimigo %i!"%(dano_joga,escolha))
	elif acao == 2:
		print(sp)
		if sp <= 10:
			print("Você não tem SP suficiente!")
		else:
			bonus_vida = randint(10,15)
			print("Você recebeu %i de vida!"%bonus_vida)
			vida += bonus_vida
			sp -= 10

	derr = []
	
	for i in range(inimigos):
		if vidas_ini[i] <= 0:
			dano_ini.append(0)
			print("Inimigo %i foi derrotado!"%i)
			cont += 1
			derr.append(i)
		elif randint(1,4) == 1:
			dano_ini.append(0)
			print("Inimigo %i errou o ataque!"%i)
		else:	
			dano_ini.append(randint(1,3))
			print("Inimigo %i causou %i de dano!"%(i,dano_ini[i]))

	for dano in dano_ini:
		dano_ini_tot += dano
	vida -= dano_ini_tot
	dano_ini = []
	dano_ini_tot = 0


	if sp < 100:
		sp += 3

	print (cont)	
	
if vida <= 0:
	print("Fim de jogo! Você perdeu!")
else:
	print("Parabéns! Você venceu!")
