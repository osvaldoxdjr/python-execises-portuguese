def verificaSeq(p,q):
	aux_p = p

	while q != 0:
		dig_q = q%10
		q = q//10
		dig_p = aux_p%10

		if aux_p == 0:
			break

		if dig_q == dig_p:
			aux_p = aux_p//10
		else:
			aux_p = p

	return aux_p

def main():
	p = int(input("Digite o número p: "))
	q = int(input("Digite o número q: "))

	if not(verificaSeq(p,q)):
    		print("p é subnúmero de q")
	else:
    		print("p não é subnúmero de q")

main()

