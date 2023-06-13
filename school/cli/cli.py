import os
from .rules import *
from .secondary_rules import render_other_options_menu


def start():
    options = {
        '0': exit,
        '1': insert_setor,
        '2': insert_curso,
        '3': insert_funcionario,
        '4': insert_professor,
        '5': insert_aluno,
        '6': insert_disciplina,
        '7': inscrever_aluno,
        '8': lancar_nota,
        '9': render_other_options_menu
    }

    os.system('clear')

    while True:
        print('Bem vindo ao sistema!')
        print('0) Sair')
        print('1) Cadastrar setor')
        print('2) Cadastrar curso')
        print('3) Cadastrar funcionário')
        print('4) Cadastrar professor')
        print('5) Cadastrar aluno')
        print('6) Cadastrar disciplina')
        print('7) Inscrever aluno em disciplina')
        print('8) Lançar nota')
        print('9) Mais opções')

        option = input('Escolha uma opção para continuar: ')

        action = options.get(option)

        if action == None:
            os.system('clear')
            print('Opção inválida, tente novamente!')
            continue

        os.system('clear')
        action()
        os.system('clear')
