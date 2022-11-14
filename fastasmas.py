import cores
import pygame


class Fantasmas:
    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.cor = cor
        self.col = 14
        self.lin = 12
        self.lin_inten = self.lin
        self.col_inten = self.col
        self.vel_x = 0.5
        self.vel_y = 0.5
        self.velocidade = 0.5

    def pintar_fantasma(self, tela_principal):
        co_x = int(self.tamanho * self.col)
        co_y = int(self.tamanho * self.lin)
        pygame.draw.rect(tela_principal, self.cor, (co_x + 1, co_y + 2,
                                                    self.tamanho - 2, self.tamanho - 4), 0, 2)
        # Criando desenho do olho
        olho_x1 = int(co_x + self.raio - 2)
        olho_y1 = int(co_y + self.raio - 2)

        # Criando desenho do olho
        olho_x2 = int(co_x + 2 * (self.raio - 3))
        olho_y2 = int(co_y + self.raio - 2)
        raio_olho = int(self.raio / 5)

        # printando olhos
        pygame.draw.circle(tela_principal, cores.preto, (olho_x1, olho_y1), raio_olho, 0)
        pygame.draw.circle(tela_principal, cores.preto, (olho_x2, olho_y2), raio_olho, 0)

        # criando a boca do fastasma
        boca_x = int(olho_x1 - 2)
        boca_y = int(olho_y1 + 3)

        # printando boca
        pygame.draw.rect(tela_principal, cores.preto, (boca_x, boca_y, 10, 3), 0)

        # Fantasma Triangulo
        # ponto_superior = (co_x + self.raio, co_y + 4)
        # ponto_inf_esq = (co_x + 4, co_y + (2 * self.raio) - 4)
        # pont_inf_dir = (co_x + (2 * self.raio) - 4, co_y + (2 * self.raio) - 4)
        # triangulo = [ponto_inf_esq, ponto_superior, pont_inf_dir]
        # pygame.draw.polygon(tela_principal, cores.azul, triangulo, 0)

    def process_events(self):
        pass
