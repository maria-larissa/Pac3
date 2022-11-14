import cores
import pygame


def game_over():

    tela_over = pygame.display.set_mode((800, 600), 0)
    pygame.display.set_caption('Pac3')

    while True:
        tela_over.fill(cores.preto)

        img_over = pygame.image.load("imagens/game_over-300.jpg")
        tela_over.blit(img_over, (200, 50))

        fonte = pygame.font.SysFont("times", 32, True, False)  # (fonte, tamanho, negrito, itálico)
        pygame.draw.rect(tela_over, cores.branco, (200, 380, 400, 1), 0)
        text_over = "Tente novamente!"
        img_14 = fonte.render(text_over, True, cores.branco)
        tela_over.blit(img_14, (270, 460))

        pygame.display.update()

        for eve in pygame.event.get():
            if eve.type == pygame.QUIT or eve.type == pygame.KEYDOWN:
                exit()
