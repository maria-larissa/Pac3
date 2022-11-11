from pacman import PacmanAnimacao
import cores
import pygame

pygame.init()

tela_animacao = pygame.display.set_mode((800, 600), 0)
pacman = PacmanAnimacao(800 // 30)
pacman.posicao()
tela_animacao.fill(cores.preto)

while True:
    pacman.posicao()
    tela_animacao.fill(cores.preto)

    # titulo jogo
    fonte = pygame.font.SysFont("times", 100, True, False)  # (fonte, tamanho, negrito, itálico)
    titulo_jogo = "Pac3"
    img_titulo = fonte.render(titulo_jogo, True, cores.azul_escuro)
    tela_animacao.blit(img_titulo, (305, 157))
    img_titulo = fonte.render(titulo_jogo, True, cores.vermelho)
    tela_animacao.blit(img_titulo, (295, 155))
    img_titulo = fonte.render(titulo_jogo, True, cores.branco)
    tela_animacao.blit(img_titulo, (300, 150))

    fonte1 = pygame.font.SysFont("times", 25, True, False)  # (fonte, tamanho, negrito, itálico)
    aperte_tecla = "Aperte qualquer tecla!"
    img_apertetecla = fonte1.render(aperte_tecla, True, cores.branco)
    tela_animacao.blit(img_apertetecla, (270, 320))

    pacman.pac_setup(tela_animacao)
    pygame.display.update()
    pygame.time.delay(200)

