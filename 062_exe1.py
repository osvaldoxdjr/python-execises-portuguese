"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenchida --> bool
    cor_de_contorno --> inteiro
 
Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura
 
Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro  
"""
from math import pi

class ObjetoGrafico(object):
	def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno):
		self.cor_de_preenchimento = cor_de_preenchimento
		self.preenchida = preenchida
		self.cor_de_contorno = cor_de_contorno

class Retangulo(ObjetoGrafico):
	def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
		super(Retangulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
		self.base = base
		self.altura = altura
	
	def area(self):
		return self.base*self.altura

	def perimentro(self):
		return self.base*2+self.altura*2

class Circulo(ObjetoGrafico):
	def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, raio):
		super(Circulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
		self.raio = raio
	
	def area(self):
		return pi*self.raio**2

	def perimentro(self):
		return 2*pi*self.raio

class Triangulo(ObjetoGrafico):
	def __init__(self, cor_de_preenchimento, preenchida, cor_de_contorno, base, altura):
		super(Triangulo, self).__init__(cor_de_preenchimento, preenchida, cor_de_contorno)
		self.base = base
		self.altura = altura
	
	def area(self):
		return (self.base*self.altura)/2

	def perimentro(self):
		return self.base+self.altura+((self.base)**2+self.altura**2)**(1/2)
