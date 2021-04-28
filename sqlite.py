import sqlite3
from Util import formatar
from Util import formatarParenteses


def insertDado(dado):
    try:
        # Conecta o Banco
        banco = sqlite3.connect('Rola_Dado')
        # variavel cursor executa o SQL
        cursor = banco.cursor()

        # Insere dado
        cursor.execute("INSERT INTO DADO (DADO) VALUES ('" + str(dado) + "')")

        banco.commit()
        banco.close()

    except sqlite3.Error:
        print("Erro ao Inserir: ", sqlite3.Error)


def searchDado():
    try:
        # Conecta o Banco
        banco = sqlite3.connect('Rola_Dado')
        # variavel cursor executa o SQL
        cursor = banco.cursor()

        listDado = []

        for c in cursor.execute("SELECT DADO FROM DADO").fetchall():
            valorFormatado = formatarParenteses(formatar(str(c)))
            listDado.append(valorFormatado)

        return listDado




    except sqlite3.Error as erro:
        print("ERRO ao procurar: ", sqlite3.Error)


def mostrarDados():
    try:

        banco = sqlite3.connect('Rola_Dado')
        # variavel cursor executa o SQL
        cursor = banco.cursor()

        dic = {}
        # Gambiarra da Gambiarra
        for i in cursor.execute("SELECT ID FROM DADO").fetchall():
            valorFormatadoI = formatarParenteses(formatar(str(i)))
            for y in cursor.execute("SELECT DADO FROM DADO WHERE ID = " + valorFormatadoI + " "):
                valorFormatadoY = formatarParenteses(formatar(str(y)))
                dic.update({(valorFormatadoI, valorFormatadoY)})
                pass

        return dic

    # Avisa erro de sql
    except sqlite3.Error:
        print("Erro ao mostrar: ", sqlite3.Error)


def deletarTudo():
    try:
        banco = sqlite3.connect('Rola_Dado')
        cursor = banco.cursor()

        cursor.execute("DROP TABLE DADO")
        cursor.execute("CREATE TABLE DADO (ID INTEGER PRIMARY KEY AUTOINCREMENT, DADO INTEGER)")
        print("Banco deletado com Sucesso")

    except sqlite3.Error as erro:
        print("Erro ao deletar: ", erro)

# OUTROS COMANDOS
# DROP NO BANCO
# cursor.execute("DROP TABLE DADO")
# cursor.execute("CREATE TABLE DADO (ID INTEGER PRIMARY KEY AUTOINCREMENT, DADO INTEGER)")
#
# cursor.execute("INSERT INTO DADO (DADO) VALUES(20)")
#
# cursor.execute("SELECT * FROM DADO")
#
# print(cursor.fetchall())
