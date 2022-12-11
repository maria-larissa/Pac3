from tela_instrucoes import *
from tela_about import *
from jogo import loop_principal
import cores
import pygame


class Ponto:
    def __init__(self):
        self.centro_x = 250
        self.centro_y = 301
        self.raio = 4
        self.opcao = 1

    # Desenha o pontinho na tela para sinalizar qual o opção  ques está sendo selecionada
    def desenhar(self):
        pygame.draw.circle(tela_menu, cores.branco, (self.centro_x, self.centro_y), self.raio, 0)

    # Processa as novas posições do pontinho de acordo com a tecla clicada
    def pro_eventos(self, lista_eventos):
        for eve in lista_eventos:
            if eve.type == pygame.KEYDOWN:

                # muda a posicao do ponto de acordo com a opcao
                if eve.key == pygame.K_DOWN:
                    if self.opcao == 1:
                        self.centro_y += 50
                        self.desenhar()
                    if self.opcao == 2:
                        self.centro_y += 50
                        self.desenhar()
                    elif self.opcao == 3:
                        self.centro_y += 50
                        self.desenhar()
                    elif self.opcao == 4:
                        self.centro_y += 50
                        self.desenhar()
                    self.opcao += 1
                if eve.key == pygame.K_UP:
                    if self.opcao == 4:
                        self.centro_y -= 50
                        self.desenhar()
                    elif self.opcao == 3:
                        self.centro_y -= 50
                        self.desenhar()
                    elif self.opcao == 2:
                        self.centro_y -= 50
                        self.desenhar()
                    elif self.opcao == 1:
                        self.centro_y -= 50
                        self.desenhar()
                    self.opcao -= 1


tela_menu = pygame.display.set_mode((800, 600), 0)
pt_opcao = Ponto()


def menu():
    pygame.init()
    pygame.display.set_caption('Pac3')

    while True:
        tela_menu.fill(cores.preto)

        # Mantem o loop do pontinho nas posições especificadas
        if pt_opcao.opcao == 5 or pt_opcao.opcao == 0:
            pt_opcao.opcao = 1
            pt_opcao.centro_y = 301
            pt_opcao.desenhar()

        # Desenha o pontinho
        pt_opcao.desenhar()

        # Printa o titulo da opção "menu"
        fonte = pygame.font.SysFont("times", 38, True, False)       # (fonte, tamanho, negrito, itálico)
        titulo_menu = "Menu Principal"
        img_titulo = fonte.render(titulo_menu, True, cores.branco)  # (texto, suavização, cor)
        tela_menu.blit(img_titulo, (270, 150))

        # Printa o titulo da opção "começar"
        fonte1 = pygame.font.SysFont("times", 25, True, False)      # (fonte, tamanho, negrito, itálico)
        opcao_play = "Play"
        img_play = fonte1.render(opcao_play, True, cores.branco)
        tela_menu.blit(img_play, (260, 290))

        # Printa o titulo da opção "About"
        opcao_about = "About"
        img_about = fonte1.render(opcao_about, True, cores.branco)
        tela_menu.blit(img_about, (260, 340))

        # Printa o titulo da opção "instruções"
        opcao_about = "Instructions"
        img_instrucao = fonte1.render(opcao_about, True, cores.branco)
        tela_menu.blit(img_instrucao, (260, 390))

        # Printa o titulo da opção "sair"
        opcao_sair = "Exit"
        img_sair = fonte1.render(opcao_sair, True, cores.branco)
        tela_menu.blit(img_sair, (260, 440))

        pygame.display.update()                         # Update da tela
        pygame.time.delay(50)
        eventos = pygame.event.get()                    # Armazena os eventos da tela
        pt_opcao.pro_eventos(eventos)                   # Processa os eventos do pontinho

        # Processa os eventos da tela
        for e in eventos:
            # Saber qual a opcao selecionada e ir para a tela correspondente
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN or e.key == pygame.K_KP_ENTER:
                    if pt_opcao.opcao == 1:
                        loop_principal()
                    elif pt_opcao.opcao == 2:
                        about()
                    elif pt_opcao.opcao == 3:
                        instrucao()
                    elif pt_opcao.opcao == 4:
                        exit()
            if e.type == pygame.QUIT:
                exit()
