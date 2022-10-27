from pacman import Pacman
from cenarios import *
import cores
import pygame

pygame.init()


fase = 1
tamanho = 640 // 30                     # Definição tamanho do pacman e dos retângulos

# Criando tela
tela_principal = pygame.display.set_mode((640, 480), 0)     # Criando a tela do jogo
pacman = Pacman(tamanho)                                           # criando um objeto do tipo Pacman
cen = Cenario(tamanho, fase)                         # Criando objeto do tipo Cenário

while True:
    pacman.posicao()                                # Callando posições do pacman
    tela_principal.fill(cores.preto)                      # Limpando a tela, para mnão aparecer rastros
    cen.pintar_cenario(tela_principal)          # Pintando o cenário
    pacman.pac_setup(tela_principal)                # Pintando pacman
    pygame.display.update()                         # atualizando o tela_principal
    pygame.time.delay(3)                            # Delay para ver a nova tela
    eventos = pygame.event.get()                    # Armazenando os eventos
    pacman.process_events(eventos)                  # Processando os eventos
