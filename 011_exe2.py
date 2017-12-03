"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a<=b<=c:
    print("Menor:",a,"Maior:",c)
elif a<=c<=b:
    print("Menor:",a,"Maior:",b)
elif b<=a<=c:
    print("Menor:",b,"Maior:",c)
elif b<=c<=a:
    print("Menor:",b,"Maior:",a)
elif c<=a<=b:
    print("Menor:",c,"Maior:",b)
else:
    print("Menor:",c,"Maior:",a)  
