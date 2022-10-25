import pygame

pygame.init()

amarelo = (255, 255, 0)
preto = (0, 0, 0)


class Pacman:

    def __init__(self):      # Definicao de tamanho, raio e centro.
        self.centro_x = 320
        self.centro_y = 240
        self.tamanho = 640 // 30
        self.raio = self.tamanho // 2
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.col = 1
        self.lin = 1

    # Funcao para criar e pintar o pacman
    def pac_setup(self, tela_principal):
        pygame.draw.circle(tela_principal, amarelo, (self.centro_x, self.centro_y), self.raio, 0)

    # criando as coordenadas da boca do pacman
        canto_da_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_da_boca, labio_superior, labio_inferior]

    # Criando o desenho da boca
        pygame.draw.polygon(tela_principal, preto, pontos, 0)

    # criando as coordenadas do olho do pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.65)
        raio_olho = int(self.raio / 10)

    # Criando desenho do olho
        pygame.draw.circle(tela_principal, preto, (olho_x, olho_y), raio_olho, 0)

    # Calcula novas posicoes
    def posicao(self):
        self.col = self.col + self.velocidade_x
        self.lin = self.lin + self.velocidade_y
        self.centro_x = int(self.col * self.tamanho + self.raio)
        self.centro_y = int(self.lin + self.tamanho + self.raio)

    # Verifica  as teclas que estao sendo apertadas
    def process_events(self, eventos):
        for e in eventos:
            # Interpretador de movimentos
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0.1
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -0.1
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -0.5
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0.5
                else:
                    if e.mod & pygame.KMOD_SHIFT:
                        if e.key == pygame.K_DELETE:
                            print("Tecla secreta")

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

            if e.type == pygame.QUIT:
                exit()
