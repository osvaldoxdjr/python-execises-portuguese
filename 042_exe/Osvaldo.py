import random

def VerificaEntrada(num):
	if 1000 <= num < 10000:
		return True
	else:
		return False

def GeraSecretNum():
	secretNum = 0
	mult = 1
	list_num = []	
	num_pos = list(range(10))
	for i in range(4):
		digito = random.choice(num_pos)
		secretNum += digito * mult
		list_num.append(digito)
		num_pos.remove(digito)
		mult *= 10
	return secretNum, list_num[::-1]
	
def GeraDicas(num, secretNum, secretNumList):
	print(num, secretNum, secretNumList)
	numList = []
	dicas = []
	aux = num
	print(aux)
	if secretNum == num:

		return dicas
	for i in range(4):
		digito = aux%10
		numList.append(digito)
		aux //= 10
	numList = numList[::-1]

	for i in range(4):
		print(secretNumList.count(numList[i]))
		if secretNumList[i] == numList[i]:
			dicas.append(2)
		elif secretNumList.count(numList[i]) >= 1:
			dicas.append(1)
		
	if len(dicas) == 0:
		dicas.append(0)

	dicas.sort()

	return dicas
		
		
		
		
    
