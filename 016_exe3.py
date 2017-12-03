n = int(input("Digite o tamanho da sequência: "))
ant = int(input("Digite o número: "))

cont, seq = 1, 0          

while cont < n:
    atual = int(input("Digite o número: "))
    if atual == ant:
        seq += 1
    ant = atual
    cont += 1

print("O número de segmentos de número igual é %d" %seq)
