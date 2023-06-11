import os
from .. import repositories as repos


def insert_setor():
    while True:
        print('Cadastrar setor')
        cod_setor = int(input('Digite o codigo do setor: '))
        nome = input('Digite o nome do setor: ')

        if repos.SetoresRepository.insert(nome=nome, cod_setor=cod_setor):
            print('Setor cadastrado com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar o setor! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def insert_curso():
    while True:
        print('Cadastrar curso')
        cod_curso = int(input('Digite o codigo do curso: '))
        nome = input('Digite o nome do curso: ')
        ano_inicio = int(input('Digite o ano de início do curso: '))

        if repos.CursosRepository.insert(cod_curso=cod_curso, nome=nome, ano_inicio=ano_inicio):
            print('Curso cadastrado com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar o curso! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def insert_funcionario():
        while True:
            print('Cadastrar funcionario')
            cod_curso = int(input('Digite o codigo do curso: '))
            nome = input('Digite o nome do curso: ')
            ano_inicio = int(input('Digite o ano de início do curso: '))

            if repos.CursosRepository.insert(cod_curso=cod_curso, nome=nome, ano_inicio=ano_inicio):
                print('Curso cadastrado com sucesso!')
                input('Aperte enter para sair!')
                os.system('clear')
                return
            else:
                print('Erro ao cadastrar o curso! Tente novamente!')
                input('Aperte enter para tentar de novo!')
                os.system('clear')


def insert_professor():
    print('Cadastrar professor')
    input()


def insert_aluno():
    print('Cadastrar aluno')
    input()


def insert_disciplina():
    print('Cadastrar disciplina')
    input()


def inscrever_aluno():
    print('Inscrever aluno em uma disciplina')
    input()


def lancar_nota():
    print('Lançar nota')
    input()
