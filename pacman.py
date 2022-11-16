import pygame
import cores

pygame.init()


class Pacman:
    def __init__(self, tamanho, fant):      # Definicao das características INICIAIS do Pacman.
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.col = 1
        self.lin = 1
        self.col_intencao = self.col
        self.lin_intencao = self.lin
        self.velocidade = 1
        self.fase = 1
        self.vidas = 5
        self.fantasmas = fant

    # Função calcula novas posições do pacman
    def posicao(self):
        self.col_intencao = self.col + self.velocidade_x
        self.lin_intencao = self.lin + self.velocidade_y
        self.centro_x = int(self.col * self.tamanho + self.raio)
        self.centro_y = int(self.lin * self.tamanho + self.raio)

    # Funcao para criar e pintar o pacman
    def pac_setup(self, tela_principal):
        pygame.draw.circle(tela_principal, cores.amarelo, (self.centro_x, self.centro_y), self.raio, 0)

    # criando as coordenadas da boca do pacman
        canto_da_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_da_boca, labio_superior, labio_inferior]

    # Criando o desenho da boca
        pygame.draw.polygon(tela_principal, cores.preto, pontos, 0)

    # criando as coordenadas do olho do pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.65)
        raio_olho = int(self.raio / 10)

    # Criando desenho do olho
        pygame.draw.circle(tela_principal, cores.preto, (olho_x, olho_y), raio_olho, 0)

    # Verifica  as teclas que estao sendo apertadas
    def process_events(self, eventos, tela):
        for e in eventos:
            # Interpretador de movimentos do pacman

            # Quando apertar uma das teclas
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = self.velocidade
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -self.velocidade
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -self.velocidade
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = self.velocidade
                else:
                    if e.mod & pygame.KMOD_SHIFT:                   # tecla secreta
                        if e.key == pygame.K_DELETE:

                            # reseta as posições do pacman e dos fantasmas
                            if 1 <= self.fase <= 3:
                                self.fase += 1
                                self.centro_x = 400
                                self.centro_y = 300
                                self.velocidade_x = 0
                                self.velocidade_y = 0
                                self.col = 1
                                self.lin = 1
                                self.col_intencao = self.col
                                self.lin_intencao = self.lin
                                for j in range(0, 5):
                                    self.fantasmas[j].lin = 1
                                    self.fantasmas[j].col = 27
                                    self.fantasmas[j].pintar_fantasma(tela)

            # quanfo soltar uma das teclas
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

    def prox_posicao(self):
        self.lin = self.lin_intencao
        self.col = self.col_intencao


class PacmanAnimacao:
    def __init__(self, tamanho):      # Definicao de tamanho, raio e centro.
        self.centro_x = 8
        self.centro_y = 450
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.velocidade_x = 1
        self.velocidade = 30

    def pac_setup(self, tela_principal):
        pygame.draw.circle(tela_principal, cores.amarelo, (self.centro_x, self.centro_y), self.raio, 0)

    # criando as coordenadas da boca do pacman
        canto_da_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_da_boca, labio_superior, labio_inferior]

    # Criando o desenho da boca
        pygame.draw.polygon(tela_principal, cores.preto, pontos, 0)

    # criando as coordenadas do olho do pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.65)
        raio_olho = int(self.raio / 10)

    # Criando desenho do olho
        pygame.draw.circle(tela_principal, cores.preto, (olho_x, olho_y), raio_olho, 0)

    def posicao(self):
        self.centro_x = self.centro_x + self.velocidade
        if self.centro_x - self.raio <= 0:
            self.velocidade = 30
        if self.centro_x + self.raio >= 800:
            self.velocidade = -30
