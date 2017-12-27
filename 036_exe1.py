"""
Escreva o jogo dos números como descrito na aula. Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser
 
Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2
"""
import random
matriz = []
n = m = 4
ganhou_jogo = False

def geraMatriz(matriz):	
	lista = list(range(1,n*m))+['#']
	for i in range(n):
		linha = []
		for j in range(m):
			x = random.choice(lista)
			linha.append(x)
			lista.remove(x)
		matriz.append(linha)

def trocaElemento(pos1, pos2, matriz):
	elemento1 = matriz[pos1//10-1][pos1%10-1]
	elemento2 = matriz[pos2//10-1][pos2%10-1]
	matriz[pos1//10-1][pos1%10-1] = elemento2
	matriz[pos2//10-1][pos2%10-1] = elemento1

def VerificaSeVenceu(matriz):
	global ganhou_jogo
	jogo_gabarito = [['#',1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
	if matriz == jogo_gabarito:
		ganhou_jogo = True
		print("Parabéns! Você venceu o jogo!")		

def VerificaJogada(pos, matriz):
	if 11<=pos<=44:
		for i in range(n):
			for j in range(m):
				if matriz[i][j] == '#':
					indice = i*10+j+11
		aux = indice
		if aux+10 == pos:
			status_jogada = True
		elif aux-10 == pos:
			status_jogada = True	
		elif aux+1 == pos:
			status_jogada = True
		elif aux-1 == pos:
			status_jogada = True
		else:
			status_jogada = False
			print("Não é possível executar a jogada!")
		return status_jogada, indice
	else:
		status_jogada = False
		print("Não é possível executar a jogada!")
		return status_jogada, 0
	

def ImprimeJogo(matriz):
	for i in range(n):
		for j in range(m):
			if matriz[i][j] == '#':
				print("%4c"%matriz[i][j], end = '')
			else:
				print("%4i "%matriz[i][j], end = '')
		print("\n")

def main():
	#geraMatriz(matriz)
	matriz = [[1,2,3,'#'],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
	ImprimeJogo(matriz)	
	opcao = int(input("Deseja inserir uma posição? (0 - Não / 1 - Sim): "))
	while opcao and not(ganhou_jogo):
		pos = int(input("Digite a posição a ser inserida: "))
		status_jogada, indice = VerificaJogada(pos,matriz)	
		if status_jogada:
			trocaElemento(pos, indice, matriz)
		VerificaSeVenceu(matriz)
		ImprimeJogo(matriz)
		if not(ganhou_jogo):
			opcao = int(input("Deseja inserir uma posição? (0 - Não / 1 - Sim): "))
	print("Obrigado por jogar!")
main()
			
