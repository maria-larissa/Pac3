from pacman import Pacman
from cenarios import Cenario
import cores
import pygame


def loop_principal():
    pygame.init()

    tela_principal = pygame.display.set_mode((800, 600), 0)     # Criando a tela do jogo
    tamanho = 600 // 30                                         # Definição tamanho do pacman e dos retângulos
    pacman = Pacman(tamanho)                                    # criando um objeto do tipo Pacman
    cen = Cenario(tamanho, pacman)                    # Criando objeto do tipo Cenário

    while True:

        pacman.posicao()                                # Calculando posições do pacman
        cen.teste_colisao_pac()                         # Testando a intenção de movimento do pacman
        tela_principal.fill(cores.preto)                # Limpando a tela, para não aparecer rastros
        cen.pintar_cenario(tela_principal)              # Pintando o cenário
        pacman.pac_setup(tela_principal)                # Pintando pacman
        cen.informacoes(tela_principal)                 # Printa informações do jogo
        pygame.display.update()                         # atualizando o tela_principal
        pygame.time.delay(100)                          # Delay para ver a nova tela
        eventos = pygame.event.get()                    # Armazenando os eventos
        pacman.process_events(eventos)                  # Processando os eventos
