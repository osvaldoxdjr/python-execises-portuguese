"""
Escreva o jogo do chute.
Nele você deve sortear um número inteiro entre 1 e 100 e pedir
para o usuário advinhar o número que você escolheu
 
Para cada chute do usuário você deve imprimir uma dica, se
ele chutou baixo de mais ou alto demais
 
Uma vez que o usuário acerte o chute o programa imprime uma
mensagem e também o número de chutes que o usuário deu
 
OBS: Use o statement break
 
Exemplo:
 
>>>
Tente advinhar o número que eu estou pensando
Seu Chute: 50
Você deve chutar mais alto!
Seu Chute: 75
Você deve chutar mais alto!
Seu Chute: 87
Você deve chutar mais alto!
Seu Chute: 93
Você deve chutar mais alto!
Seu Chute: 97
Você deve chutar mais baixo!
Seu Chute: 95
Parabens você acertou!!
Você chutou 6 vezes
>>>
 """
import random

def verificaJogada(num_tentativa, num_gabarito):
	if num_tentativa == num_gabarito:
		print("Parabéns você acertou!")
		return True

	if num_tentativa < num_gabarito:
		print("Você deve chutar mais alto!")	
	elif num_tentativa > num_gabarito:
		print("Você deve chutar mais baixo!")
	return False

def main():
	print("Tente adivinha o número que estou pensando")
	num_gabarito = random.randint(1,100)
	cont = 0
	while(True):
		num_tentativa = int(input("Seu chute: "))
		if verificaJogada(num_tentativa, num_gabarito):
			break
		cont += 1
	print("Você chutou %i vezes"%cont)
main()
	
	
