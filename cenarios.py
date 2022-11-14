from tela_congratulations import tela_congra
import pygame
import cores
# Como funciona o cálculo
'''
    2- parede
    1 - comida
    0 - vazio

    coordenadas retnagulos
    tamanho = 800 // 30
    x = col * tamanho
    y = lin * tamanho

    fase1 = 325 pontos
    fase2 = 385 pontos
    fase3 = 321 ponto
'''


class Cenario:

    # Quando chamar a classe é passado o tamanho qual a tela em que sera printado o cenario
    # o tamanho que terá o cenrio e qual sera a matriz correspondente a fase atual
    def __init__(self, tamanho, pacman, fantasma):
        self.pacman = pacman
        self.fantasma = fantasma
        self.fase = self.pacman.fase
        self.aux = self.fase           # Utilizada para sempre guardar a fase antiga, para pode atualizar o novo cenário
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz = [
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            ]
        self.acima = 1
        self.baixo = 2
        self.direita = 3
        self.esquerda = 4

    # Função atualiza informações necessárias do cenário ao clicar na tecla secreta
    # ou ao comer todas as comidas e chgar no portão
    def novo_cenario(self):
        if self.fase == 2:
            self.aux = self.fase                    # atualiza variável aux
            self.matriz = [
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            ]           # atualiza matriz
            self.pontos = 0                         # zera pontos
        elif self.fase == 3:
            self.aux = self.fase                    # atualiza variável aux
            self.pacman = self.pacman
            self.matriz = [
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2],
                [2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2],
                [2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                [2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2],
                [2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            ]           # atualiza matriz
            self.pontos = 0                         # zera pontos

    # Varre a linha dada para pintar cada retâgulo da cor certa de cada coluna da linha passada
    def pintar_coluna(self, tela_principal, n_linha, linha):
        for n_coluna, coluna in enumerate(linha):
            # calculando as coordenadas do canto superior de cada retângulo da matriz
            co_x = n_coluna * self.tamanho
            co_y = n_linha * self.tamanho

            # Escolhendo a cor de acordo com a fase
            cor = cores.preto
            if self.fase == 1:
                cor = cores.verde
            elif self.fase == 2:
                cor = cores.laranja
            elif self.fase == 3:
                cor = cores.vermelho

            # pinta cada retângulo com a cores certas e coloca comida
            if coluna == 2:
                # pinta parede
                pygame.draw.rect(tela_principal, cor, (co_x, co_y, self.tamanho, self.tamanho), 0)

            if coluna == 1:
                # coordenadas da comida
                x_comida = co_x + self.tamanho // 2
                y_comida = co_y + self.tamanho // 2
                # pinta comida
                pygame.draw.circle(tela_principal, cores.branco, (x_comida, y_comida), self.tamanho // 10, 0)

            if coluna == 0:
                # pinta espaço vazio
                cor = cores.preto
                pygame.draw.rect(tela_principal, cor, (co_x, co_y, self.tamanho, self.tamanho), 0)

    #  Varre todas as linhas da matriz pra pintar os retângulos
    def pintar_cenario(self, tela_principal):
        self.fase = self.pacman.fase
        if self.fase != self.aux and self.fase <= 3:
            self.novo_cenario()
        for n_linha, linha in enumerate(self.matriz):
            self.pintar_coluna(tela_principal, n_linha, linha)

    # printar informações do jogo na tela
    def informacoes(self, tela_principal):

        if self.fase == 4:
            tela_congra()
            pass

        # fase
        fonte_fase = pygame.font.SysFont("times", 36, True, False)          # (fonte, tamanho, negrito, itálico)
        texto_fase = "Fase: {}".format(str(self.fase))
        if self.fase == 1:
            img_fase = fonte_fase.render(texto_fase, True, cores.verde)
            tela_principal.blit(img_fase, (620, 200))
        elif self.fase == 2:
            img_fase = fonte_fase.render(texto_fase, True, cores.laranja)
            tela_principal.blit(img_fase, (620, 200))
        elif self.fase == 3:
            img_fase = fonte_fase.render(texto_fase, True, cores.vermelho)
            tela_principal.blit(img_fase, (620, 200))

        # pontos
        fonte_pontos = pygame.font.SysFont("times", 32, True, True)     # (fonte, tamanho, negrito, itálico)
        texto_pontos = "Pontos: {}".format(str(self.pontos))
        img_pontos = fonte_pontos.render(texto_pontos, True, cores.branco)
        tela_principal.blit(img_pontos, (612, 300))

    def posicao_fantasma(self, linha, coluna):
        direcoes = []                       # criando a lista de possibilidades de movimento

        # verifica as posições
        if self.matriz[linha][coluna] != 2:
            # verifica se pode mover para cima
            if self.matriz[linha-1][coluna] != 2:
                direcoes.append(self.acima)

            # verifica se pode mover para baixo
            if self.matriz[linha + 1][coluna] != 2:
                direcoes.append(self.baixo)

            # verifica se pode mover para esquerda
            if self.matriz[linha][coluna - 1] != 2:
                direcoes.append(self.esquerda)

            # verifica se pode mover para direita
            if self.matriz[linha][coluna + 1] != 2:
                direcoes.append(self.direita)
        return direcoes

    # Função teste se o pacman pode se mover para a nova posição desejada
    # retira comida quando o pacman passa
    def teste_colisao(self):
        direcoes_possiveis = self.posicao_fantasma(self.fantasma.lin, self.fantasma.col)
        print(direcoes_possiveis)

        nova_col = self.pacman.col_intencao
        nova_lin = self.pacman.lin_intencao
        if 0 <= nova_col < 29 and 0 <= nova_lin < 30:
            if self.matriz[nova_lin][nova_col] != 2:                # Caso a posição NÃO seja parede
                self.pacman.prox_posicao()

                if self.matriz[nova_lin][nova_col] == 1:            # Caso tenha comida aumenta pontos e apaga a comida
                    self.pontos += 1
                    self.matriz[nova_lin][nova_col] = 0

                if self.matriz[nova_lin][nova_col] == 0:            # verificar se comeu tudo e chegou no centro(portal)

                    # verifica se chegou no centro
                    if nova_lin in range(13, 16) and nova_col in range(12, 15):

                        # verifica se comeu tudo de acordo com a fase
                        if self.pontos == 325 or self.pontos == 385 or self.pontos == 321:

                            # print("fase")
                            # print(self.fase)

                            self.aux = self.fase                            # Guarda valor anterior da fase
                            self.pacman.fase += 1                           # Incrementa a fase, faz passar de fase

                            # Faz pacman voltar pra posição inicial
                            self.pacman.centro_x = 400
                            self.pacman.centro_y = 300
                            self.pacman.velocidade_x = 0
                            self.pacman.velocidade_y = 0
                            self.pacman.col = 1
                            self.pacman.lin = 1
                            self.pacman.col_intencao = self.pacman.col
                            self.pacman.lin_intencao = self.pacman.lin

                            self.novo_cenario()                             # Atualiza cenário

