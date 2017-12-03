raiz = 32

num = raiz*raiz

while num < 10000:
    auxMaior = num//100
    auxMenor = num%100
    if (auxMaior + auxMenor) == (raiz):
        print(num)
    raiz += 1
    num = raiz*raiz
