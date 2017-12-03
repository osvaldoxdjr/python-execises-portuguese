"""
Faça um Programa para uma loja de tintas.
 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.
 
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.
 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if
"""

# Input do usuário
area = int(input("Digite o valor da area: "))
area = int(area*1.1+1)

# Número de litros para a area desejada
litros = area//6

if area%6 > 0:
    litros = litros + 1


# Verificando condição I
latas_18 = litros//18

if litros%18 > 0:
    latas_18 = latas_18 + 1
    
# Verificando condição II
latas_4 = litros//4

if litros%18 > 0:
    latas_4 = latas_4 + 1

# Verificando condição III
latas_18_i = litros//18

if litros%18 <= 12:
        latas_4_i = litros%18//4
        if litros%18%4 > 0:
            latas_4_i = latas_4_i + 1
else:
    latas_18_i = latas_18_i+1
    latas_4_i = 0

print("A quantidade de tinta a ser comprada eh:", litros)
print("Cond I: Latas de 18L =", latas_18, "-- R$", latas_18*80)
print("Cond II: Latas de 4L =", latas_4, "-- R$", latas_4*25)
print("Cond III: Latas de 18L =", latas_18_i, "-- Latas de 4L =", latas_4_i, "-- R$",
      latas_18_i*80+latas_4_i*25)
