import cores
import pygame


def tela_congra():

    tela_cong = pygame.display.set_mode((800, 600), 0)

    while True:
        tela_cong.fill(cores.preto)

        img_trofeu = pygame.image.load("imagens/trofeus/trofeu-100.jpg")
        tela_cong.blit(img_trofeu, (300, 100))

        fonte = pygame.font.SysFont("times", 32, True, False)  # (fonte, tamanho, negrito, itálico)
        pygame.draw.rect(tela_cong, cores.branco, (200, 350, 400, 1), 0)
        text_congra = "Parabéns"
        text_win = "Você ganhou o jogo!"
        img_12 = fonte.render(text_congra, True, cores.branco)
        img_13 = fonte.render(text_win, True, cores.branco)
        tela_cong.blit(img_12, (330, 400))
        tela_cong.blit(img_13, (250, 430))

        pygame.display.update()

        for eve in pygame.event.get():
            if eve.type == pygame.QUIT or eve.type == pygame.KEYDOWN:
                exit()
