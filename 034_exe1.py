"""
Faça um programa com uma função chamada somaImposto.
 
A função possui dois parâmetros formais:
    1 - taxaImposto, que é a quantia de imposto sobre vendas expressa em
        porcentagem
    2 - custo, que é o custo de um item antes do imposto.
 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto, custo):
	return custo*(1+taxaImposto/100)

taxaImposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo: "))

print("O valor total do custo é:",somaImposto(taxaImposto, custo))
