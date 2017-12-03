"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
 
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
    três notas de 100, uma nota de 50, quatro notas de 10,
    uma nota de 5 e quatro notas de 1.
// %
"""

saque = int(input("Digite a quantia de dinheiro para saque: "))

if 10 <= saque <= 600:

    n100 = saque//100
    resto = saque%100
    n50 = resto//50
    resto = resto%50
    n10 = resto//10
    resto = resto%10
    n5 = resto//5
    resto = resto%5
    n1 = resto//1
    
    print("Número de notas de R$ 100:", n100);
    print("Número de notas de R$ 50:", n50);
    print("Número de notas de R$ 10:", n10);
    print("Número de notas de R$ 5:", n5);
    print("Número de notas de R$ 1:", n1);

else:
    print("Não é possivel sacar menos de 10 reais ou mais de 600 reais!")

