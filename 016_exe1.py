n = int(input("Digite um número: "))
valor, alg, soma = n, 0, 0

while valor != 0:
    alg += 1
    valor = valor//10

resto = n
while alg >= 0:
    som_val = resto%10
    resto = resto//10
    soma += som_val*10**(alg-1)
    alg -= 1
    
if soma == n:
    print("O número %d é palíndromo"%n)
