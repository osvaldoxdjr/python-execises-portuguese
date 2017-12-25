"""
Reescreva o simulador da megasena de forma que agora em vez de trabalhar com
o mesmo jogo sempre, o programa seleciona aleatoriamento o jogo do teórico
jogador. Faça apenas um teste a não ser que você resolva deixar o pc ligado
o dia inteiro.
"""

import random

meu = []

megasena = list(range(1,61))

meu_jogo = megasena.copy()

for k in range(6):
	jogo_sort = random.choice(meu_jogo)
	meu.append(jogo_sort)
	meu_jogo.remove(jogo_sort)
 
n = int(input("Número de testes: "))
 
soma = 0
 
for i in range(n):
    sorteado = []
 
    cont = 0
 
    while meu != sorteado:
        mega_sort = megasena.copy()
 
        sorteado = []
 
        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)
 
        sorteado.sort()
 
        cont += 1
 
    soma += cont
 
    print("Resultado do teste %i: %i tentativas"%(i+1, cont))
 
soma /= n
 
print("Média dos resultados:", soma)
