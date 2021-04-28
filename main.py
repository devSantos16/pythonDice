from builtins import dict

from Jogada import Jogada
from Jogada import mostrarTodosOsDados
from Jogada import deletar
from Jogada import verificarDadoNulo

# Modo usuario
loop = True

while loop:
    menu = int(input("SEJA BEM VINDO! \n"
                     "Digite o modo de entrada\n"
                     "1 - Modo Admin\n"
                     "2 - Modo Usuário\n"
                     "0 - Sair do Programa\n"
                     "Digite a opção: "))

    if menu == 0:
         exit(4)

    elif menu == 1:
        menuUsuario = int(input("MENU DO USUARIO\n"
                                "1 - Mostrar dados e jogar\n"
                                "2 - Adicionar Dado e jogar\n"
                                "3 - Mostrar todas as jogadas\n"
                                "4 - Deletar Tudo\n"
                                "0 - SAIR\n"
                                "Digite a opção desejada: "))

        if menuUsuario == 0:
            print("SAINDO !!! ")
            exit(4)

        if menuUsuario == 1:
            f = mostrarTodosOsDados()
            verificarDadoNulo(f)
            print("Todos os dados inseridos: ")

            for c in range(len(f)):
                print(f[c])
            resultado = int(input("Digite qual dado tu quer: "))

            for c in range(len(f)):

                if f[c] == str(resultado):
                    j = Jogada(resultado)
                    print(j.retornarDado())

        elif menuUsuario == 2:
            resultado = int(input("Digite um numero para o Dado: "))
            j = Jogada(resultado)
            print(j.retornarDado())

        elif menuUsuario == 3:
            mostrarTodosOsDados()

        elif menuUsuario == 4:
            print("Deletando tudo")
            deletar()

        else:
            print("ERRO, Digite novamente");

    elif menu == 2:
        print("Ok!")
        exit(4)

    else:
        print("ERRO, tente novamente !")

# resultado = int(input("Digite um numero para o Dado: "))
#
# j = Jogada(resultado)
#
# print(j.retornarDado())
