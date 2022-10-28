import pygame
import cores

pygame.init()


class Pacman:
    # Larissa: Atualizei a característica tamanho do pacman de "640 // 30"
    # para tanho que varia de acordo com o tamanho dos retangulos
    def __init__(self, tamanho):      # Definicao de tamanho, raio e centro.
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

    # Função calcula novas posições
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
    def process_events(self, eventos):
        for e in eventos:
            # Interpretador de movimentos
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
                    if e.mod & pygame.KMOD_SHIFT:
                        if e.key == pygame.K_DELETE:
                            print(self.fase)
                            print("Tecla secreta")
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
                            else:
                                print("Congratulations!")

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
