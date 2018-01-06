"""
Classe Retangulo: Crie uma classe que modele um retangulo:
 
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e
calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
a quantidade de pisos necessárias para o local.
"""

class Retangulo(object):
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def mudarValor(self, base_nova, altura_nova):
		self.base = base_nova
		self.altura = altura_nova

	def retornaValor(self):
		return self.base, self.altura

	def calculaArea(self):
		return self.base*self.altura

	def calculaPerimetro(self):
		return self.base*2+self.altura*2
		
