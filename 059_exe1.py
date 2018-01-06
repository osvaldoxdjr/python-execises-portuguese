"""
Classe Quadrado: Crie uma classe que modele um quadrado:
 
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:

	def __init__(self, lado):
		self.lado = lado

	def mudaValor(self, novo_valor):
		self.lado = novo_valor

	def retornaValor(self):
		return self.lado

	def calculaArea(self):
		return self.lado**2
