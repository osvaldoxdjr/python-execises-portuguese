"""
Escreva um jogo de sobrevivência, no qual o player irá escolher entre
continuar, salvar e desistir.

CONTINUAR --> O jogo escolherá 1 entre 4 inimigos para lutar com o player,
SALVAR --> Salva o estado do player e o número de inimigos derrotados
DESISTIR --> Salva um arquivo de Score contendo o tanto de inimigos que o
player derrotou

O combate:
Cada personagem do jogo possuí os seguintes atributos:
Player --> For 20, Def 20, HP 500 e SP 100
Ogro --> For 30, Def 5, HP 100 e SP 5
Goblin --> For 15, Def 10, HP 70 e SP 10
Esqueleto --> For 20, Def 20, HP 80 e SP 20
Bruxo --> For 10, Def 30, HP 80 e SP 20

O jogador pode escolher entre os seguintes ataques:
Espadada, Flexada, Cura, Lança de Gelo

Já os inimigos
Ogro --> Clavada
Goblin --> Flexada
Esqueleto --> Espadada, Cura
Bruxo --> Relampago, Bola de Fogo, Espadada, Cura

A cada final de batalha o jogador pode escolher entre aumentar em 5 o valor
de um atributo ou recuperar todo HP ou recuperar todo SP

A cada 10 inimigos derrotados o número de inimigos em uma batalha dobra, e o
player os enfrenta SIMULTANEAMENTE

O calculo de dano é:
Espada --> max((For - Def)*random(0,1), 1) consumo de SP 0
Flexada --> max((For - Def/3)*random(0,1), 1) consumo de SP 2
Clavada --> max((For - Def/1)*random(0,1), 1) consumo de SP 0
Relampago --> max((For - Def/5)*random(0,1), 1) consumo de SP 5
BolaDeFogo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
LançaDeGelo --> max((For - Def/5)*random(0,1), 1) consumo de SP 10
Cura --> recupera 10 consumo de SP 10
"""

import random

Player = {"Nome": "Player", "For": 20, "Def": 20, "HP": 500, "SP": 100, "Ataques": ["Espadada", "Flexada", "Cura", "Lança de Gelo"]}
Ogro = {"Nome": "Ogro", "Dados": {"For": 30, "Def": 5, "HP": 100, "SP": 5}, "Ataques": ["Clavada"]}
Goblin = {"Nome": "Goblin", "For": 15, "Def": 10, "HP": 70, "SP": 10, "Ataques": ["Flexada"]}
Esqueleto = {"Nome": "Esqueleto", "For": 20, "Def": 20, "HP": 80, "SP": 20, "Ataques": ["Espadada","Cura"]}
Bruxo = {"Nome": "Bruxo", "For": 10, "Def": 30, "HP": 80, "SP": 20, "Ataques": ["Relampago", "Bola de Fogo", "Espadada", "Cura"]}

Jogadores = {"Player": Player, "Ogro": Ogro, "Goblin": Goblin, "Esqueleto": Esqueleto, "Bruxo": Bruxo}

nomes_inimigo = ["Goblin", "Esqueleto", "Bruxo", "Ogro"]
Playerd = ["Player", 500, 100]
inimigos = []
n_inimigos = 1

ataques = {	"Espadada": (lambda For, Def, rand: max((For - Def)*rand, 1), 0),
		"Flexada": (lambda For, Def, rand: max((For - Def/3)*rand, 1), 2),
		"Clavada": (lambda For, Def, rand: max((For - Def/1)*rand, 1), 0),
		"Relampago": (lambda For, Def, rand: max((For - Def/5)*rand, 5)),
		"Bola de Fogo": (lambda For, Def, rand: max((For - Def/5)*rand, 1), 10), 
		"Lança de Gelo": (lambda For, Def, rand: max((For - Def/5)*rand, 1), 10)
		}


def carregaInimigo(inimigo):
	nome = Jogadores[inimigo]["Nome"]
	print(nome)
	HP = Jogadores[inimigo]["HP"]
	SP = Jogadores[inimigo]["SP"]
	return [nome, HP, SP]

def escolheAtaque():
	i = int(input("Deseja usar Espadada, Flexada, Cura, Lança de Gelo?\n"))
	return (i-1)

def main():

	jogando = input("Deseja iniciar um novo jogo (s/novo) ou sair (n/sair)? ")
	while jogando == 's':
		jogando = input("Deseja enfrentar um novo inimigo (s/combate) ou sair (n/sair)? ")
		if jogando == 'n':
			break
		nome_jogador = input("Digite o nome do jogador: ")
		print("HP: %.2f"%Player["HP"])
		print("SP: %.2f"%Player["SP"])

		inimigo = carregaInimigo(random.choice(nomes_inimigo))
		inimigos.append(inimigo)
		
		print("Escolhe um alvo dentre:")
		
		for i in range(n_inimigos):
			print("%i - %s HP: %.2f/ SP = %.2f"%(i+1, inimigos[i][0], inimigos[i][1], inimigos[i][2]))
		
		alvo = int(input(""))-1
		
		while Playerd[1] > 0 and inimigos[alvo][1] > 0:
			
			print("HP: %.2f"%(Playerd[1]))
			print("SP: %.2f"%(Playerd[2]))

			ataque_nome_player = Jogadores["Player"]["Ataques"][escolheAtaque()]
			ataque_nome_inimigo = random.choice(Jogadores[inimigos[alvo][0]]["Ataques"])
			rand1 = random.random()
			rand2 = random.random()
			
			if ataque_nome_player == "Cura":
				if Playerd[2] > 10:
					Playerd[1] += 10
					Playerd[2] -= 10
					print("%s se curou em 10!"%s)
				else:
					print("Você não tem SP suficiente!")

			else:
				dano, Perda_SP = ataques[ataque_nome_player]

				if Playerd[2] > Perda_SP:
					print("%s usou %s em %s"%(nome_jogador, ataque_nome_player.upper(),inimigos[alvo][0]))
					Playerd[2] -= Perda_SP
					dano_num = dano(Player["For"], Player["Def"], rand1)
					inimigos[alvo][1] -= dano_num
					print("%s causou %.2f de dano!"%(nome_jogador, dano_num))
				else:
					print("%s não tem SP suficiente!"%nome_jogador)
			
			if ataque_nome_inimigo == "Cura":
				print(inimigo[alvo][2])
				if inimigos[alvo][2] > 10:
					inimigos[alvo][1] += 10
					inimigos[alvo][2] -= 10
					print("%s se curou em 10!"%inimigo[alvo][0])
				else:
					print("O %s não tem SP suficiente!"%inimigos[alvo][0])

			else:

				dano, Perda_SP = ataques[ataque_nome_inimigo]

				if inimigos[alvo][2] > Perda_SP:
					print("%s usou %s em Player"%(inimigos[alvo][0], ataque_nome_inimigo.upper()))
					inimigos[alvo][2] -= Perda_SP
					dano_num = dano(Jogadores[inimigos[alvo][0]]["For"],
							Jogadores[inimigos[alvo][0]]["Def"], rand2)
					Playerd	[1] -= 	dano_num
					print("%s causou %.2f de dano!"%(inimigos[alvo][0],dano_num))
				else:
					print("O %s não tem SP suficiente!"%inimigos[alvo][0])

			if inimigos[alvo][1] > 0:
				print("%i - %s HP: %.2f/ SP = %.2f"%(i+1, inimigos[alvo][0], 
					inimigos[alvo][1], inimigos[alvo][2]))
			else:
				print("Você eliminou o inimigo!")

			Playerd[2] += 5
			inimigos[alvo][2] += 10			

main()	
		
		
