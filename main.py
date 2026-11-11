import random
import os
import time
import keyboard
import numpy 

tabuleiro = [[0 for coluna in range(11)]for linha in range(21)] 

for linha in range(len(tabuleiro)):

    tabuleiro[linha][0] = 3
    tabuleiro[linha][10] = 3

    for coluna in range (len(tabuleiro[linha])):
        if tabuleiro[20][coluna] == 0:
            tabuleiro[20][coluna] = 2

#peças

peca_0 =[
    [1,1],
    [1,1]
]

peca_1 =[
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

peca_2 =[
    [1,1,1],
    [0,1,0],
    [0,0,0]
]

pecas = [peca_0, peca_1, peca_2]

Pe = randomiza_pecas(pecas)

#posição inicial da peça no tabuleiro

x_peca = 4

y_peca = 0

X = 4

Y = 0

pontostotais = 0

pode_descer = True

rodando = True


def imprime_tabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] !=0:
                print("██" ,end="")
            else:
                print("  ", end="")
        print()
    
def limpa_tabuleiro(tabuleiro):

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == 0 or tabuleiro[linha][coluna] == 1:
                tabuleiro[linha][coluna] = 0

def pontos(tabuleiro):

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):

            if tabuleiro[i][j] == 4:

                if sum(tabuleiro[i]) == 42:

                    pont = 1

                    tabuleiro[i] = [0] *len(tabuleiro[i])
                    tabuleiro[i][0] = 3
                    tabuleiro[i][10] = 3 

                    return(pont)
    return(0)


def desenhar_peca(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == 1:

                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca
                
                tabuleiro[linha][coluna] = 1

def colisao(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == 1:
                
                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca

                if tabuleiro[linha+1][coluna] == 2 or tabuleiro[linha+1][coluna] == 4:
                    
                    return(False)

    return(True)

def decisao(y_peca):
    
    if pode_descer == True:

        y_peca+=1

        return(y_peca)
    
    else:

        return(y_peca)

def fixar(tabuleiro):

    for i in range(len(tabuleiro)):

        for j in range(len(tabuleiro[i])):

            if tabuleiro[i][j] == 1:

                tabuleiro[i][j] = 4

def randomiza_pecas(pecas):
    Pe = random.choice(pecas)
    return(Pe)

#Movimento
def girarPe(Pe):

    Pe = numpy.rot90(Pe)
    return(Pe)

def mexer_peca_esquerda(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == 1:

                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha-1][coluna-1] == 2 or tabuleiro[linha-1][coluna-1] == 3 or tabuleiro[linha-1][coluna-1] == 4:
                    
                        return(+0)

    return(-1)

def mexer_peca_direita(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == 1:

                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha+1][coluna+1] == 2 or tabuleiro[linha+1][coluna+1] == 3 or tabuleiro[linha+1][coluna+1] == 4:
                    
                        return(+0)

    return(+1)

def mexer_peca_baixo(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == 1:

                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha+1][coluna] == 2 or tabuleiro[linha+1][coluna] == 3:
                    
                        return(+0)

    return(+1)

#while do jogo

while rodando:

    os.system("cls")

    pontostotais += pontos(tabuleiro)

    if keyboard.is_pressed('r'):

        Pe = girarPe (Pe)

    if keyboard.is_pressed('left'):
        
        x_peca += mexer_peca_esquerda(Pe,x_peca,y_peca)

        X +=mexer_peca_esquerda(Pe,x_peca,y_peca)

    if keyboard.is_pressed('right'):

        x_peca += mexer_peca_direita(Pe,x_peca,y_peca)

        X +=mexer_peca_direita(Pe,x_peca,y_peca)

    if keyboard.is_pressed('down'):

        y_peca += mexer_peca_baixo(Pe,x_peca,y_peca)

        Y +=mexer_peca_baixo(Pe,x_peca,y_peca)

    limpa_tabuleiro(tabuleiro)

    pode_descer = colisao (Pe,x_peca,y_peca)
    
    if pode_descer == False:

        desenhar_peca(Pe,x_peca,y_peca)

        fixar (tabuleiro)

        x_peca = 4
        y_peca = 0

        X = 4
        Y = 0

        Pe = randomiza_pecas(pecas)

    if pode_descer == True:

        y_peca = decisao (y_peca)

        desenhar_peca(Pe,x_peca,y_peca)

    imprime_tabuleiro(tabuleiro)

    print(pontostotais)

    if tabuleiro[0][4] == 4:
        rodando = False

    time.sleep(0.4)

print("FIM DO JOGO")