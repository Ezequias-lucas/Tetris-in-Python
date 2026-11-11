import random
import os
import time
import keyboard
import numpy 

#CONSTANTES DE ORGANIZAÇÂO E LEGIBILIDADE

VAZIO = 0
PECA_MOVEL = 1
CHAO = 2
PAREDE = 3
PECA_FIXA = 4

tabuleiro = [[VAZIO for coluna in range(11)]for linha in range(21)] 

for linha in range(len(tabuleiro)):

    tabuleiro[linha][0] = PAREDE
    tabuleiro[linha][10] = PAREDE

    for coluna in range (len(tabuleiro[linha])):
        if tabuleiro[20][coluna] == VAZIO:
            tabuleiro[20][coluna] = CHAO

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

def randomiza_pecas(pecas):
    Pe = random.choice(pecas)
    return(Pe)

Pe = randomiza_pecas(pecas)

#posição inicial da peça no tabuleiro

x_peca = 4

y_peca = 0

X = 4

Y = 0

pontostotais = 0

pode_descer = True


def rodando(tabuleiro):

    if tabuleiro[0][4] == PECA_FIXA:
        return(False)
    else:
        return(True)

loop_jogo = rodando(tabuleiro)

def imprime_tabuleiro(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] != VAZIO:
                print("██" ,end="")
            else:
                print("  ", end="")
        print()
    
def limpa_tabuleiro(tabuleiro):

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == VAZIO or tabuleiro[linha][coluna] == PECA_MOVEL:
                tabuleiro[linha][coluna] = VAZIO

def pontos(tabuleiro):

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):

            if tabuleiro[i][j] == PECA_FIXA:
                if sum(tabuleiro[i]) == 42:

                    pont = 1

                    tabuleiro[i] = [0] *len(tabuleiro[i])
                    tabuleiro[i][0] = PAREDE
                    tabuleiro[i][10] = PAREDE

                    return(pont)
    return(0)


def desenhar_peca(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:

                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca
                
                tabuleiro[linha][coluna] = PECA_MOVEL

def colisao(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                
                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca

                if tabuleiro[linha+1][coluna] == CHAO or tabuleiro[linha+1][coluna] == PECA_FIXA:
                    
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

            if tabuleiro[i][j] == PECA_MOVEL: 

                tabuleiro[i][j] = PECA_FIXA

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
            if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:

                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca

                if tabuleiro[linha-1][coluna-1] == CHAO \
                    or tabuleiro[linha-1][coluna-1] == PAREDE \
                        or tabuleiro[linha-1][coluna-1] == PECA_FIXA:
                
                    return(+0)

    return(-1)

def mexer_peca_direita(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:

                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca

                if tabuleiro[linha+1][coluna+1] == CHAO \
                    or tabuleiro[linha+1][coluna+1] == PAREDE \
                        or tabuleiro[linha+1][coluna+1] == PECA_FIXA:
                    
                    return(+0)

    return(+1)

def mexer_peca_baixo(Pe,x_peca,y_peca):

    for linha_da_peca in range(len(Pe)):
        for coluna_da_peca in range(len(Pe[linha_da_peca])):
            if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:

                coluna = coluna_da_peca + x_peca
                linha = linha_da_peca + y_peca

                if tabuleiro[linha+1][coluna] == CHAO \
                    or tabuleiro[linha+1][coluna] == PECA_FIXA:
                
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

    rodando(tabuleiro)

    time.sleep(0.4)

print("FIM DO JOGO")