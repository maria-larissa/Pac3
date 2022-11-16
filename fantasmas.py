import random
import cores
import pygame


# Função que cria e retorna um vetor (lista) com 5 fantasmas
def lista_fantasmas(tamanho):
    fantasma1 = Fantasmas(tamanho, cores.vermelho_intenso)  # criando um objeto do tipo Fantasma
    fantasma2 = Fantasmas(tamanho, cores.azul_escuro)       # criando um objeto do tipo Fantasma
    fantasma3 = Fantasmas(tamanho, cores.rosa)              # criando um objeto do tipo Fantasma
    fantasma4 = Fantasmas(tamanho, cores.roxo)              # criando um objeto do tipo Fantasma
    fantasma5 = Fantasmas(tamanho, cores.verde_claro)       # criando um objeto do tipo Fantasma

    lista = [fantasma1, fantasma2, fantasma3, fantasma4, fantasma5]     # Crio a lista
    return lista


class Fantasmas:

    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.cor = cor
        self.lin = 1
        self.col = 27
        self.direcao = 1
        self.lin_inten = self.lin
        self.col_inten = self.col
        self.velocidade = 1

    # Função define para qual direção vai o fantasma
    def posicao(self):
        if self.direcao == 1:
            self.lin_inten -= self.velocidade
        elif self.direcao == 2:
            self.lin_inten += self.velocidade
        elif self.direcao == 3:
            self.col_inten -= self.velocidade
        elif self.direcao == 4:
            self.col_inten += self.velocidade

    def pintar_fantasma(self, tela_principal):
        co_x = int(self.tamanho * self.col)
        co_y = int(self.tamanho * self.lin)
        pygame.draw.rect(tela_principal, self.cor, (co_x + 1, co_y + 2,
                                                    self.tamanho - 2, self.tamanho - 4), 0, 2)
        # Criando desenho do olho1
        olho_x1 = int(co_x + self.raio - 2)
        olho_y1 = int(co_y + self.raio - 2)

        # Criando desenho do olho2
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

    # muda a posição do fantasma caso não haja colisão com as pareddes
    def prox_posicao(self):
        self.lin = self.lin_inten
        self.col = self.col_inten

    # função auxiliar usada nas duas funções abaixo
    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    # Função que decide quando tiver 3 possibilidades de escolha pa ra a direção do fantasma
    def caso_esquina(self, direcoes):
        self.mudar_direcao(direcoes)

    # escolhe a nova posição caso haja colisão na posição anteriormente escolhida
    def permanecer_posicao(self, direcoes):
        self.lin_inten = self.lin
        self.col_inten = self.col
        self.mudar_direcao(direcoes)
