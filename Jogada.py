from builtins import list

from Dado import Dado
from sqlite import insertDado
from sqlite import mostrarDados
from sqlite import deletarTudo
from sqlite import searchDado
import random


def verificarDadoNulo(lista):
    count = 0
    for c in range(len(lista)):
        count = count + 1
    if count == 0:
        print("Não foi possivel mostrar, pois não existe")
        exit()


def mostrarTodosOsDados():
    listDado = searchDado()
    return listDado


def deletar():
    return deletarTudo()


class Jogada:

    def __init__(self, num):
        num = Dado(num)
        self.dado = num.dado

    def retornarDado(self):
        resultado = random.randint(1, self.dado)
        insertDado(self.dado)
        return resultado
