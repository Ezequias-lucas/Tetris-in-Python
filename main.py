import random
import os
import time
import keyboard
import numpy 
from audioplayer import AudioPlayer

musica = AudioPlayer("Original Tetris theme (Tetris Soundtrack).mp3")
musica.volume = 30
musica.play(loop=True)

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
peca_4 =[
    [1,1,1],
    [1,0,0]
]
peca_5 =[
    [1,1,1],
    [0,0,1]
]

pecas = [peca_0, peca_1, peca_2, peca_4, peca_5]

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

velocidade = 0.5

def rodando(tabuleiro):

    if tabuleiro[0][4] == PECA_FIXA:
        return(False)
    else:
        return(True)

loop_jogo = rodando(tabuleiro)

def imprime_tabuleiro(tabuleiro,cor):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == PAREDE or \
                tabuleiro[linha][coluna] ==  CHAO:
                print("\033[0;30m██" ,end="")
            elif tabuleiro[linha][coluna] == PECA_MOVEL:
                print(f"\033[0;{cor}m██" ,end="")
            elif tabuleiro[linha][coluna] == PECA_FIXA:
                print("\033[0;37m██" ,end="")
            else:
                print("  ", end="")
        print()

#Limpa o Tabuleiro Mantendo as posiçoes das pecas ja fixada

def limpa_tabuleiro(tabuleiro):

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna] == VAZIO \
                or tabuleiro[linha][coluna] == PECA_MOVEL:
                tabuleiro[linha][coluna] = VAZIO

def desenhar_peca(Pe,x_peca,y_peca):
    try:
        for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    tabuleiro[linha][coluna] = PECA_MOVEL
    except IndexError: 
        for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                    coluna = coluna_da_peca
                    linha = linha_da_peca

                    tabuleiro[linha][coluna] = PECA_MOVEL

#Verifica se a colisao no movimento seguinte

def colisao(Pe,x_peca,y_peca):
    try:
        for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha+1][coluna] == CHAO \
                        or tabuleiro[linha+1][coluna] == PECA_FIXA:
                        return(False)

        return(True)
    except IndexError:   
        return(True)

#Mantem o movimento de queda da peca

def gravidade(y_peca):
    try:    
        if pode_descer == True:
            y_peca+=1
            return(y_peca)
        else:
            return(y_peca)
    except IndexError:   
        return (y_peca)

def descer_peca(tabuleiro, linha_limpa):
    try:
        for i in range(linha_limpa, 0, -1):
            for j in range (1, 10):
                tabuleiro[i][j] = tabuleiro[i-1][j]
    except IndexError:   
        return (0)

def pontos(tabuleiro):

    for i in range(len(tabuleiro)):
        if sum(tabuleiro[i][1:10]) == 9* PECA_FIXA:
            for j in range(1, 10):
                tabuleiro[i][j] = VAZIO

                descer_peca(tabuleiro,i)

                return(1000)

    return(0)


def fixar(tabuleiro):

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == PECA_MOVEL: 
                tabuleiro[i][j] = PECA_FIXA

#Movimento

def girar_peca_escolhida(Pe):
    try:
        Pe = numpy.rot90(Pe)
        return(Pe)
    except IndexError:
        return(Pe)

def mexer_peca_esquerda(Pe,x_peca,y_peca):
    try:
        for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha][coluna-1] == CHAO \
                        or tabuleiro[linha][coluna-1] == PAREDE \
                            or tabuleiro[linha][coluna-1] == PECA_FIXA:
                    
                        return(+0)

        return(-1)
    except IndexError:
        return(0)

def mexer_peca_direita(Pe,x_peca,y_peca):
    try:
        for linha_da_peca in range(len(Pe)):
            for coluna_da_peca in range(len(Pe[linha_da_peca])):
                if Pe[linha_da_peca][coluna_da_peca] == PECA_MOVEL:
                    coluna = coluna_da_peca + x_peca
                    linha = linha_da_peca + y_peca

                    if tabuleiro[linha][coluna+1] == CHAO \
                        or tabuleiro[linha][coluna+1] == PAREDE \
                            or tabuleiro[linha][coluna+1] == PECA_FIXA:
                        
                        return(+0)

        return(+1)
    except IndexError:
        return (0)

#while do jogo

cor = 30

while loop_jogo:
    os.system("cls")
    pontostotais += pontos(tabuleiro)
    if not(keyboard.is_pressed('left') or keyboard.is_pressed('right')):
        if keyboard.is_pressed('r'):
            Pe = girar_peca_escolhida(Pe)

    if keyboard.is_pressed('left'):
        x_peca += mexer_peca_esquerda(Pe,x_peca,y_peca)
        X +=mexer_peca_esquerda(Pe,x_peca,y_peca)

    if keyboard.is_pressed('right'):
        x_peca += mexer_peca_direita(Pe,x_peca,y_peca)
        X +=mexer_peca_direita(Pe,x_peca,y_peca)

    limpa_tabuleiro(tabuleiro)
    pode_descer = colisao (Pe,x_peca,y_peca)
    
    if pode_descer == False:
        cor = 30
        desenhar_peca(Pe,x_peca,y_peca)
        fixar (tabuleiro)
        velocidade *= 0.96

        x_peca = 4
        y_peca = 0
        X = 4
        Y = 0

        Pe = randomiza_pecas(pecas)
        cor += random.randrange(0,8)

    if pode_descer == True:
        y_peca = gravidade (y_peca)
        desenhar_peca(Pe,x_peca,y_peca)

    imprime_tabuleiro(tabuleiro,cor)
    print(pontostotais)
    loop_jogo = rodando(tabuleiro)
    print(velocidade)
    time.sleep(velocidade)

print("FIM DO JOGO")