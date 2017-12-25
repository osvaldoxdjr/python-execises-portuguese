"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.
"""

def converteHoras(horas,minutos):
	if horas < 12:
		m_meio_dia = False
		horas_pm = horas
	else:
		m_meio_dia = True
		horas_pm = horas-12

	return horas_pm, minutos, m_meio_dia

def mostraHoras(horas, minutos, m_meio_dia):
	if m_meio_dia == True:
		print("O horário é %d:%d P.M."%(horas,minutos))
	else:
		print("O horário é %d:%d A.M."%(horas,minutos))	

n = 0

while n == 0:
	n = int(input("Quer realizar a conversão de horas? ([0]Sim / [1]Não): "))
	h = int(input("Digite as horas: "))
	m = int(input("Digite os minutos: "))
	horas_pm, minutos, m_meio_dia = converteHoras(h,m)
	mostraHoras(horas_pm, minutos, m_meio_dia)
