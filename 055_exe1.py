"""
Escreva um programa que receba quantas entradas o usuário desejar e depois
crie um novo contato para cada entrada (Nome, Telefone, Endereço, Email), e
por fim imprima, em ordem alfabética, a agenda de contatos 
"""

INFOS = ("Nome", "Telefone", "Endereço", "Email")
Lista_Contatos = {}
Dados = []

def recebeDados(Dados, num_contato):
	global INFO
	for INFO in INFOS:
		Dados.append(input("Digite o %s do contato %i: "%(INFO, num_contato)))

def criaContato(Dados):
	global INFOS
	contato = {	INFOS[0]: Dados[0], 
			INFOS[1]: Dados[1],
			INFOS[2]: Dados[2],
			INFOS[3]: Dados[3],	}
	return contato

def adicionaContato(contato, num_contato):
	global Lista_Contatos
	Lista_Contatos["Contato " + str(num_contato)] = contato

def imprimeContatos(Lista_Contatos):

	ordem = []
	i = 0
	for contato in Lista_Contatos:
		if ordem == []:
			ordem.append(contato)
		else:
			print(Lista_Contatos[ordem[i]]["Nome"].upper(), Lista_Contatos[contato]["Nome"].upper())
			if Lista_Contatos[ordem[i]]["Nome"].upper() >  Lista_Contatos[contato]["Nome"].upper():
				ordem.insert(0,contato)
			else:
				ordem.append(contato)
			i += 1
	
	for elemento in ordem:
		print(Lista_Contatos[elemento])

def main():
	Dados = []
	global Lista_Contatos

	n = int(input("Digite o número de contatos que deseja inserir: "))
	for i in range(n):
		recebeDados(Dados, i+1)
		adicionaContato(criaContato(Dados), i+1)
		Dados = []
	imprimeContatos(Lista_Contatos)

main()

	
		

	
