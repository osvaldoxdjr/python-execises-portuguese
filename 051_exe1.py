"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":
 
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
 
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:
 
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
 
1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%
 
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
 
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""

CONV_MB_CONST = 1024.0**2

def convParaMB(tamanhosMBString):
	total_ocupado = 0
	for i in range(len(tamanhosMBString)):
		aux = float(tamanhosMBString[i])/CONV_MB_CONST
		total_ocupado += aux
		tamanhosMBString[i] = "%.2f MB"%aux
	return total_ocupado

def calculoPercentual(percentualString, total_ocupado):
	for i in range(len(percentualString)):
		aux = float(percentualString[i])*100/CONV_MB_CONST
		percentualString[i] = "%.2f%%"%(aux/total_ocupado)

def separaDados(dados, nomes, tamanhos):
	for dado in dados:
		nomes.append(dado.split()[0]) 
		tamanhos.append(dado.split()[1])

def main():
	nomes = []
	tamanhos = []

	arquivo = open('usuarios.txt', 'r')
	dados = arquivo.readlines()
	
	arquivo.close()

	separaDados(dados, nomes, tamanhos)

	tamanhosMBString = tamanhos.copy()
	percentualString = tamanhos.copy()

	total_ocupado = convParaMB(tamanhosMBString)
	calculoPercentual(percentualString, total_ocupado)

	cabecalho = "ACME Inc.               Uso do espaço em disco pelos usuários"
	cabecalho += "------------------------------------------------------------------------\n"
	cabecalho += "Nr.  Usuário        Espaço utilizado     %% do uso\n"
	
	mensagem = ""

	for i in range(len(tamanhos)):
		mensagem += "%i"%(i+1) + ' '*4 + nomes[i] + ' '*(25-len(nomes[i])-len(tamanhosMBString[i]))
		mensagem += tamanhosMBString[i] + ' '*(19 - len(percentualString[i])) + percentualString[i] + "\n"
		
	mensagem += "\n\nEspaço total ocupado %.2f MB\n"%total_ocupado
	mensagem += "Espaço médio ocupado %.2f MB"%(total_ocupado/len(tamanhos))

	mensagem = mensagem.replace(".",",")
	mensagem = cabecalho + mensagem
	
	arquivo = open("relatorio.txt", 'w')
	arquivo.write(mensagem)
	arquivo.close()

main()

