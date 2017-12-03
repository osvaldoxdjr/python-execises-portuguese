p = int(input("Digite o número p: "))
q = int(input("Digite o número q: "))

aux_p = p
aux_q = q
flag = 0

while aux_q != 0:
    dig_q = aux_q%10
    aux_q = aux_q//10
    dig_p = aux_p%10
    print(dig_q)
    print(dig_p)
    print(aux_p)
    if aux_p == 0:
        flag = 1
    
    if dig_q == dig_p:
        aux_p = aux_p//10
    else:
        aux_p = p

if flag == 1:
    print("p é subnúmero de q")
else:
    print("p não é subnúmero de q")
    
