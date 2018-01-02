def main():
    perguntas = ['Telefonou para a vítima?', "Esteve no local do crime?",
                 "Mora perto da vítima?", "Devia para a vítima?",
                 "Já trabalhou com a vítima?"]
    classificação = ["Inocente", "Inocente", "Suspeita", "Cúmplice",
                     "Cúmplice", "Assassina"]
    cont = 0
    for pergunta in perguntas:
        resp = input(pergunta)
 
        if tudoMinusculo(resp) == 'sim':
            cont += 1
 
    print(classificação[cont])
 
def tudoMinusculo(palavra):
    minusculo = ""
    for char in palavra:
        if ord('A') <= ord(char) <= ord('Z'):
            char = chr(ord(char) - (ord('A') - ord('a')))
 
        minusculo += char
 
    return minusculo
 
main()
