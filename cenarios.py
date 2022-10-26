import pygame

verde = (0, 255, 128)
preto = (0, 0, 0)
branco = (255, 255, 255)

class Cenario:

    # Quando chamar a classe é passado o tamanho qual a tela em que sera printado o cenario
    # o tamanho que terá o cenrio e qual sera a matriz correspondente a fase atual
    def __init__(self, tamanho, fase):
        self.tamanho = tamanho
        self.fase = fase
        if self.fase == 1:
            self.matriz = [
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 1, 2, 2, 0, 0, 2, 2, 1, 1, 2],
                [2, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2],
                [2, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2],
                [2, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2],
                [2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            ]
        elif self.fase == 2:
            self.matriz = [
                [2, 2, 2, 2, 2],
                [2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2],
                [2, 2, 2, 2, 2]
            ]
        else:
            self.matriz = [
                [2, 2, 2, 2, 2],
                [2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2],
                [2, 2, 2, 2, 2]
            ]

    # Varre a linha dada para pintar cada retâgulo da cor certa de cada coluna da linha passada
    def pintar_coluna(self, tela_principal, n_linha, linha):
        for n_coluna, coluna in enumerate(linha):
            # calculando as coordenadas do canto superior de cada retângulo da matriz
            co_x = n_coluna * self.tamanho
            co_y = n_linha * self.tamanho
            # print(co_x, co_y)
            # Escolhendo a cor
            if self.fase == 1:
                if coluna == 2:
                    cor = verde
                    pygame.draw.rect(tela_principal, cor, (co_x, co_y, self.tamanho, self.tamanho), 0)
                if coluna == 1:
                    cor = preto
                    x_comida = int(co_x + self.tamanho // 2)
                    y_comida = int(co_y + self.tamanho // 2)
                    # print(x_comida, y_comida)
                    pygame.draw.rect(tela_principal, cor, (co_x, co_y, self.tamanho, self.tamanho), 0)
                    pygame.draw.circle(tela_principal, branco, (x_comida, y_comida), 0.5, 0)
                if coluna == 0:
                    cor = preto
                    pygame.draw.rect(tela_principal, cor, (co_x, co_y, self.tamanho, self.tamanho), 0)

            # Desenhando o retângulo
        #                     surface        cor     pt_partida     altura          largura
        #     pygame.draw.rect(tela_principal, verde, (co_x, co_y, self.tamanho, self.tamanho), 0)

    #  Varre todas as linhas da matriz pra pintar os retângulos
    def pintar_cenario(self, tela_principal):
        for n_linha, linha in enumerate(self.matriz):
            self.pintar_coluna(tela_principal, n_linha, linha)

    # Como funciona o cálculo
    '''
        2- parede
        1 - comida
        0 - vazio
        
        coordenadas retnagulos
        tamanho = 640 // 30
        x = col * tamanho
        y = lin * tamanho
    '''