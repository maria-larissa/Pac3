from pacman import Pacman
from fantasmas import *
from cenarios import Cenario
import cores
import pygame


def loop_principal():
    pygame.init()
    pygame.display.set_caption('Pac3')
    tela_principal = pygame.display.set_mode((800, 600), 0)     # Criando a tela do jogo
    tamanho = 600 // 30                                         # Definição tamanho do pacman e dos retângulos
    fantasmas = lista_fantasmas(tamanho)
    pacman = Pacman(tamanho, fantasmas)                                    # criando um objeto do tipo Pacman
    cen = Cenario(tamanho, pacman, fantasmas)                    # Criando objeto do tipo Cenário

    while True:

        pacman.posicao()                                # Calculando posições do pacman
        tamanho = pacman.fase + 1
        if pacman.fase == 3:
                tamanho = 5
        for i in range(0, tamanho):
            fantasmas[i].posicao()                      # Calculando posições de cada fantasma
            cen.teste_colisao()                             # Testando a intenção de movimento do pacman
        tela_principal.fill(cores.preto)                # Limpando a tela, para não aparecer rastros
        cen.pintar_cenario(tela_principal)              # Pintando o cenário
        pacman.pac_setup(tela_principal)                # Pintando pacman
        for i in range(0, tamanho):
            print("linha", fantasmas[i].lin)
            print("coluna", fantasmas[i].col)
            fantasmas[i].pintar_fantasma(tela_principal)  # Pintando cada fantasma
        cen.informacoes(tela_principal)                 # Printa informações do jogo
        pygame.display.update()                         # atualizando o tela_principal
        pygame.time.delay(100)                          # Delay para ver a nova tela
        eventos = pygame.event.get()                    # Armazenando os eventos
        pacman.process_events(eventos, tela_principal)                  # Processando os eventos
