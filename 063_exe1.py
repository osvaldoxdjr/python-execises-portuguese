"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida
 
    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)
 
E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha
 
    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""
class Banco(object):
	__total = 10000
	TaxaReserva = 0.1
	__reservaExigida = __total*TaxaReserva

	def podeFazerEmprestimo(valor):
		if Banco.__total-valor > Banco.__reservaExigida:
			return True
		return False

	def MudaTotal(valor):
		Banco.__total += valor

class Conta(): 
	def __init__(self, saldo, ID, senha):
		self.saldo = saldo
		self.ID = ID
		self.senha = senha

	def deposito(self, valor, senha):
		if self.senha == senha:
			self.saldo += valor
			Banco.MudaTotal(valor)
		else:
			print("A senha está incorreta!")

	def saque(self, senha, valor):
		if self.senha == senha:
			self.saldo -= valor
			
			Banco.MudaTotal(-valor)
		else:
			print("A senha está incorreta!")

	def podeReceberEmprestimo(self, valor):
		return Banco.podeFazerEmprestimo(valor)

	def saldo(self):
		print("Seu saldo é: %.2f"%self.saldo)
