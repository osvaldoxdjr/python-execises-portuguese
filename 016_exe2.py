n = int(input("Digite o tamanho da sequência: "))
cont = seg = segMax = 1
ant = int(input("Digite o número: "))

while cont < n:
    atual = int(input("Digite o número: "))
    if atual > ant:
        seg += 1
    else:
        seg = 1
    if seg > segMax:
        segMax = seg
    ant = atual
    cont += 1
    
print("O comprimento de um segmento crescente máximo é %d" %segMax)
