"""
Escreva um programa para simular o jogo das portas. Faça um programa que tenha
a saída como a seguinte:
 
Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas
eu lhe informo que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim/ 0 - Não): 1
Ganhou um carro!
"""
from random import randrange

premio = randrange(1, 4)

print("Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!")

escolha = int(input("Escolha uma porta: "))

bode = 1
print (premio)
print (escolha)

while bode == escolha or bode == premio:
	bode += 1

print("Você escolheu a porta %i, mas eu lhe informo que na porta %i há um bode."%(escolha,bode))

troca = int(input("Deseja trocar de porta (1 - Sim/ 0 - Não): "))

if troca == 1:
	novo = 1
	while bode == novo and escolha == novo:
		novo += 1
	if novo == premio:
		print("Ganhou um carro!")
	else:
		print("Não ganhou um carro!")
else:
		if escolha == premio:
			print("Ganhou um carro!")
		else:
			print("Não ganhou um carro!")
