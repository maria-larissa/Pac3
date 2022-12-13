from cenarios import Cenario
from pacman import Pacman
import pytest


# teste da lista de possiveis possições que o fastamas pode se mover
def test_posicaofantasma():
    assert Cenario.posicao_fantasma(1, 1) == [2, 3]

    assert Cenario.posicao_fantasma(7, 21) == [1, 2, 4, 3]

    assert Cenario.posicao_fantasma(8, 22) == [1, 4, 3]


# teste para saber se a fase do cenario esta de acordo com a fase do pacman
def test_fase():
    teste_fase = Pacman.fase()
    assert Cenario.novo_cenario() == teste_fase
