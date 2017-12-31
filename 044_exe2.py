"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas
dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a
sua média, conforme a descrição acima informada (retirar o melhor e o pior salto
e depois calcular a média com as notas restantes). As notas não são informados
ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
 
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
 
Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
 
Tente colocar a impressão do resultado em um único print
"""

def main():
	num_notas = 7
	notas = []

	nome = input("Digite o nome do atleta: ")
	
	for i in range(num_notas):
		nota = float(input("Nota: "))
		notas.append(nota)
	
	mensagem = "Resultado final:\n"+"Atleta: "+nome+"\n"

	notas.sort()
	
	mensagem += "Pior nota: "+str(notas[0])+"\n"
	mensagem += "Melhor nota: "+str(notas[num_notas-1])+"\n"

	notas.remove(notas[0])
	num_notas -= 1
	notas.remove(notas[num_notas-1])
	
	mensagem += "Média: "+str(sum(notas)/len(notas))

	print(mensagem)

main()
