import cores
import pygame


class Ponto:
    def __init__(self):
        self.centro_x = 250
        self.centro_y = 301
        self.raio = 4
        self.opcao = 1

    def desenhar(self):
            pygame.draw.circle(tela_menu, cores.branco, (self.centro_x, self.centro_y), self.raio, 0)

    def pro_eventos(self, lista_eventos):
        for eve in lista_eventos:
            if eve.type == pygame.KEYDOWN:

                # muda a posicao do ponto de acordo com a opcao
                if eve.key == pygame.K_DOWN:
                    print(self.opcao)
                    print(self.centro_y)
                    if self.opcao == 1:
                        self.centro_y += 100
                        self.desenhar()
                    if self.opcao == 2:
                        self.centro_y += 100
                        self.desenhar()
                    elif self.opcao == 3:
                        self.centro_y += 100
                        self.desenhar()
                    elif self.opcao == 4:
                        self.centro_y += 100
                        self.desenhar()
                    self.opcao += 1
                if eve.key == pygame.K_UP:
                    print(self.opcao)
                    if self.opcao == 2:
                        self.centro_y -= 100
                        self.desenhar()
                    elif self.opcao == 3:
                        self.centro_y -= 100
                        self.desenhar()
                    elif self.opcao == 4:
                        self.centro_y -= 100
                        self.desenhar()
                    self.opcao -= 1


pygame.init()

tela_menu = pygame.display.set_mode((800, 600), 0)
pt_opcao = Ponto()

while True:
    # o ponto sempre varias nas três posições estabelecidas

    tela_menu.fill(cores.preto)
    pt_opcao.desenhar()

    if pt_opcao.opcao == 5:
        pt_opcao.opcao = 1

    # titulo menu
    fonte = pygame.font.SysFont("times", 38, True, False)  # (fonte, tamanho, negrito, itálico)
    titulo_menu = "Menu Principal"
    img_titulo = fonte.render(titulo_menu, True, cores.branco)
    tela_menu.blit(img_titulo, (270, 150))

    # opções
    fonte1 = pygame.font.SysFont("times", 25, True, False)  # (fonte, tamanho, negrito, itálico)
    opcao_play = "Play"
    img_play = fonte1.render(opcao_play, True, cores.branco)
    tela_menu.blit(img_play, (260, 290))

    opcao_about = "About"
    img_about = fonte1.render(opcao_about, True, cores.branco)
    tela_menu.blit(img_about, (260, 490))

    opcao_about = "Instructions"
    img_instrucao = fonte1.render(opcao_about, True, cores.branco)
    tela_menu.blit(img_instrucao, (260, 390))

    pygame.display.update()
    pygame.time.delay(50)
    eventos = pygame.event.get()
    pt_opcao.pro_eventos(eventos)

    for e in eventos:
        # Saber qual a opcao selecionada e ir para a tela correspondente
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER:
                if pt_opcao.opcao == 1:
                    print("Começar o jogo!")
                elif pt_opcao.opcao == 2:
                    print("Instruções!")
                elif pt_opcao.opcao == 3:
                    print("About!")
                elif pt_opcao.opcao == 4:
                    exit()
