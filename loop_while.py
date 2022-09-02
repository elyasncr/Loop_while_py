"""
Loop While:

Forma geral:

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5
num < 5



#Exemplo 1:
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1 #Se não estiver um ponto de saída, não é possível sair do loop. neste caso, o numero + 1 é a saída até o número ser menor do que zero.
# OBS: em um loop, while é importante que cuidemos do critério de parada para não cauar um loop infinito.
"""

#Exemplo 2:

resposta = ' '

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
