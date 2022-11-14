import cores
import pygame


def seta_esq(tela):
    tamanho = 16
    x_set_esq = 100 - tamanho
    y_set_esq = 180
    set_esq1 = (x_set_esq - tamanho, y_set_esq - 3)
    set_esq2 = (x_set_esq - (tamanho + 3), y_set_esq)
    set_esq3 = (x_set_esq - tamanho, y_set_esq + 3)
    seta_esquerda = [set_esq1, set_esq2, set_esq3]
    pygame.draw.polygon(tela, cores.branco, seta_esquerda, 0)
    pygame.draw.rect(tela, cores.branco, (x_set_esq - tamanho, y_set_esq, tamanho, 2), 0)
    x_caixa_esq = x_set_esq - tamanho - 10
    y_caixa_esq = y_set_esq - 11
    largura_esq = tamanho + 20
    altura_esq = tamanho + 11
    pygame.draw.rect(tela, cores.branco, (x_caixa_esq, y_caixa_esq, largura_esq, altura_esq), 2, 5)


def seta_dir(tela):
    tamanho = 16
    x_set_dir = 155
    y_set_dir = 180
    set_dir1 = (x_set_dir, y_set_dir - 3)
    set_dir2 = (x_set_dir + 3, y_set_dir)
    set_dir3 = (x_set_dir, y_set_dir + 3)
    seta_direita = [set_dir1, set_dir2, set_dir3]
    pygame.draw.polygon(tela, cores.branco, seta_direita, 0)
    pygame.draw.rect(tela, cores.branco, (x_set_dir - tamanho, y_set_dir, tamanho, 2), 0)
    x_caixa_dir = x_set_dir - tamanho - 8
    y_caixa_dir = y_set_dir - 11
    largura_dir = tamanho + 20
    altura_dir = tamanho + 11
    pygame.draw.rect(tela, cores.branco, (x_caixa_dir, y_caixa_dir, largura_dir, altura_dir), 2, 5)


def seta_cim(tela):
    tamanho = 16
    x_set_cim = 110
    y_set_cim = 140
    set_cim1 = (x_set_cim - 3, y_set_cim)
    set_cim2 = (x_set_cim, y_set_cim - 3)
    set_cim3 = (x_set_cim + 3, y_set_cim)
    seta_cima = [set_cim1, set_cim2, set_cim3]
    pygame.draw.polygon(tela, cores.branco, seta_cima, 0)
    pygame.draw.rect(tela, cores.branco, (x_set_cim, y_set_cim, 2, tamanho), 0)
    x_caixa_cim = x_set_cim - 12
    y_caixa_cim = y_set_cim - 10
    largura_cim = tamanho + 11
    altura_cim = tamanho + 20
    pygame.draw.rect(tela, cores.branco, (x_caixa_cim, y_caixa_cim, largura_cim, altura_cim), 2, 5)


def seta_bai(tela):
    tamanho = 16
    x_set_bai = 110
    y_set_bai = 190 + tamanho
    set_bai1 = (x_set_bai - 3, y_set_bai + tamanho)
    set_bai2 = (x_set_bai, y_set_bai + tamanho + 3)
    set_bai3 = (x_set_bai + 3, y_set_bai + tamanho)
    seta_baixo = [set_bai1, set_bai2, set_bai3]
    pygame.draw.polygon(tela, cores.branco, seta_baixo, 0)
    pygame.draw.rect(tela, cores.branco, (x_set_bai, y_set_bai, 2, tamanho), 0)
    x_caixa_bai = x_set_bai - 12
    y_caixa_bai = y_set_bai - 8
    largura_bai = tamanho + 11
    altura_bai = tamanho + 20
    pygame.draw.rect(tela, cores.branco, (x_caixa_bai, y_caixa_bai, largura_bai, altura_bai), 2, 5)


def instrucao():

    tela_instrucao = pygame.display.set_mode((800, 600), 0)
    pygame.init()
    pygame.display.set_caption('Instructions')

    while True:
        tela_instrucao.fill(cores.preto)

        fonte = pygame.font.SysFont("times", 32, True, False)  # (fonte, tamanho, negrito, itálico)
        titulo_instrucao = "Instruções do jogo"
        img_1 = fonte.render(titulo_instrucao, True, cores.branco)
        tela_instrucao.blit(img_1, (260, 30))

        fonte1 = pygame.font.SysFont("times", 18, True, True)  # (fonte, tamanho, negrito, itálico)
        titulo_teclas = "1- Quais teclas devo usar?"
        img_2 = fonte1.render(titulo_teclas, True, cores.branco)
        tela_instrucao.blit(img_2, (30, 90))
        seta_dir(tela_instrucao)
        seta_esq(tela_instrucao)
        seta_cim(tela_instrucao)
        seta_bai(tela_instrucao)

        titulo_objetivo = "2- Objetivo"
        img_3 = fonte1.render(titulo_objetivo, True, cores.branco)
        tela_instrucao.blit(img_3, (30, 270))

        fonte_texto = pygame.font.SysFont("times", 16, False, False)  # (fonte, tamanho, negrito, itálico)
        obj_linha1 = "    Você deve pegar todas as comidinhas de cada fase"
        obj_linha2 = "e chegar ao portal, localizado no centro de cada fase,"
        obj_linha3 = "sem encostar em nenhum fantama."
        img_4 = fonte_texto.render(obj_linha1, True, cores.branco)
        img_5 = fonte_texto.render(obj_linha2, True, cores.branco)
        img_6 = fonte_texto.render(obj_linha3, True, cores.branco)
        tela_instrucao.blit(img_4, (30, 300))
        tela_instrucao.blit(img_5, (30, 315))
        tela_instrucao.blit(img_6, (30, 330))

        titulo_fases = "3- Número de fases"
        img_7 = fonte1.render(titulo_fases, True, cores.branco)
        tela_instrucao.blit(img_7, (30, 390))
        texto_fase = "     O jogo possui apanas 3 fases."
        img_8 = fonte_texto.render(texto_fase, True, cores.branco)
        tela_instrucao.blit(img_8, (30, 415))

        # fonte2 = pygame.font.SysFont("times", 18, True, False)  # (fonte, tamanho, negrito, itálico)
        # opcao_voltar = "Voltar"
        # img_voltar = fonte2.render(opcao_voltar, True, cores.branco)
        # tela_instrucao.blit(img_voltar, (690, 530))
        # pygame.draw.circle(tela_instrucao, cores.branco, (682, 539), 4, 0)

        pygame.display.update()

        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                exit()
