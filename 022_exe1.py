"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.
 
o   Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:
 
o   salários até R$ 280,00 (incluindo) : aumento de 20%
o   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o   salários de R$ 1500,00 em diante : aumento de 5%
 
Após o aumento ser realizado, informe na tela:
o   o salário antes do reajuste;
o   o percentual de aumento aplicado;
o   o valor do aumento;
o   o novo salário, após o aumento.
 
"""

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
	perc = 1.2	
elif 280 < salario <= 700:
	perc = 1.15	
elif 700 < salario <= 1500:
	perc = 1.1	
else:
	perc = 1.05

print("Salário antes do reajuste: %.2f"%salario)
print("Percentual do aumento: %.2f"%(perc-int(perc)))
print("Valor do aumento: %.2f"%((perc-int(perc))*salario))
print("Novo salário: R$ %.g"%(salario*perc))
