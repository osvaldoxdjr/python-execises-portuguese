"""
Dados n e dois numeros inteiros positivos i e j diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são multiplos de i ou
de j e ou de ambos
 
Exemplo: Para n = 6 , i = 2 e j = 3 a saida devera ser : 0,2,3,4,6,8.
"""

n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))

nat, cont = 0, 0

while cont < n:
    if nat % i == 0 or nat % j == 0:
        print (nat)
        cont =cont+ 1
    nat = nat + 1
