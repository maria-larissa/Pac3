import cores
import pygame


def about():
    tela_about = pygame.display.set_mode((800, 600), 0)
    pygame.display.set_caption('Pac3')

    while True:
        # Titulo "sobre"
        tela_about.fill(cores.preto)
        fonte = pygame.font.SysFont("times", 32, True, False)  # (fonte, tamanho, negrito, itálico)
        titulo_about = "Sobre"
        img_1 = fonte.render(titulo_about, True, cores.branco)
        tela_about.blit(img_1, (360, 30))

        # Subtitulo "criadores"
        fonte1 = pygame.font.SysFont("times", 20, True, True)  # (fonte, tamanho, negrito, itálico)
        titulo_criadores = "Criadores"
        img_2 = fonte1.render(titulo_criadores, True, cores.branco)
        tela_about.blit(img_2, (360, 140))

        # Informações "Maria Larissa"
        fonte_texto = pygame.font.SysFont("times", 18, False, False)  # (fonte, tamanho, negrito, itálico)
        aut1_lin1 = "Maria Larissa da Silva Andrade"
        aut1_lin2 = "Graduanda em Matemática computacional"
        aut1_lin3 = "Universidde Federal do Cariri"
        aut1_lin4 = "maria.larissa@ufca.edu.br"
        img_3 = fonte_texto.render(aut1_lin1, True, cores.branco)
        img_4 = fonte_texto.render(aut1_lin2, True, cores.branco)
        img_5 = fonte_texto.render(aut1_lin3, True, cores.branco)
        img_6 = fonte_texto.render(aut1_lin4, True, cores.branco)
        tela_about.blit(img_3, (290, 190))
        tela_about.blit(img_4, (255, 205))
        tela_about.blit(img_5, (295, 220))
        tela_about.blit(img_6, (305, 235))

        # Informações "Nazareno Mateus"
        aut2_lin1 = "Nazareno Mateus de Sousa"
        aut2_lin2 = "Graduando em Matemática computacional"
        aut2_lin3 = "Universidde Federal do Cariri"
        aut2_lin4 = "nazareno.mateus@ufca.edu.br"
        img_7 = fonte_texto.render(aut2_lin1, True, cores.branco)
        img_8 = fonte_texto.render(aut2_lin2, True, cores.branco)
        img_9 = fonte_texto.render(aut2_lin3, True, cores.branco)
        img_10 = fonte_texto.render(aut2_lin4, True, cores.branco)
        tela_about.blit(img_7, (305, 315))
        tela_about.blit(img_8, (255, 330))
        tela_about.blit(img_9, (295, 345))
        tela_about.blit(img_10, (295, 360))

        pygame.draw.rect(tela_about, cores.branco, (200, 450, 400, 1), 0)
        lin_ano = "Dezembro de 2022"
        img_11 = fonte_texto.render(lin_ano, True, cores.branco)
        tela_about.blit(img_11, (330, 460))

        pygame.display.update()
