from pacman import Pacman
from cenarios import *
import cores
import pygame

pygame.init()


# Criando tela
tela_principal = pygame.display.set_mode((800, 600), 0)     # Criando a tela do jogo
tamanho = 600 // 30                     # Definição tamanho do pacman e dos retângulos
pacman = Pacman(tamanho)                              # criando um objeto do tipo Pacman
cen = Cenario(tamanho, pacman)              # MODIFIQUEI         # Criando objeto do tipo Cenário

while True:
    pacman.posicao()                                # Calculando posições do pacman
    cen.teste_colisao_pac()                         # Testando a intenção de movimento do pacman
    tela_principal.fill(cores.preto)                # Limpando a tela, para mnão aparecer rastros
    cen.pintar_cenario(tela_principal)              # Pintando o cenário
    pacman.pac_setup(tela_principal)                # Pintando pacman

    cen.informacoes(tela_principal)

    pygame.display.update()                         # atualizando o tela_principal
    pygame.time.delay(100)                          # Delay para ver a nova tela
    eventos = pygame.event.get()                    # Armazenando os eventos
    pacman.process_events(eventos)                  # Processando os eventos
