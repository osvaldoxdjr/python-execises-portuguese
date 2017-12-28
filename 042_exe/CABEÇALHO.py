import random

def VerificaEntrada(num):
	cont = 0
    	for i in range(4):
		num //= 10
		if num != 0:
			cont += 1
	if cont == 4:
		return True
	else:
		return False	

def GeraSecretNum():
	secretNum = 0
	mult = 1
	list_num = []	
	num_pos = list(range(1,11))
	for i in range(4):
		digito = random.choice(num_pos)
		secretNum = digito * mult
		list_num.append(digito)
		num_pos.remove(digito)
		mult *= 10
	return secretNum, list_num[::-1]
	
        
def GeraDicas(num, secretNum, secretNumList):
	numList = []
	dicas = []
	aux = num
	if secretNum == num:
		return dicas
	else:
		for i in range(4):
			digito = aux%10
			numList.append(digito)
			aux //= 10
		numList = numList[::-1]
	
		for i in range(4):
			if secretNumList[i] == numList[i]:
				dicas.append(2)
			elif numList.count(secretNumList[i]) >= 1
				dicas.append(1)
			else
				dicas.append(0)
	return dicas
		
		
		
		
    
