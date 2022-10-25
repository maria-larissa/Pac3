import pygame
from Pac3.pacman import Pacman

pygame.init()

preto = (0, 0, 0)

# Criando tela
tela_principal = pygame.display.set_mode((640, 480), 0)
pacman = Pacman()

while True:

    pacman.posicao()
    tela_principal.fill(preto)
    pacman.pac_setup(tela_principal)
    pygame.display.update()
    pygame.time.delay(3)
    eventos = pygame.event.get()
    pacman.process_events(eventos)