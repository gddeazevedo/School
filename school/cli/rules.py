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
        cpf = input('Digite o CPF do funcionario: ')

        while len(cpf) != 11:
            print('CPF inválido! Tente novamente')
            cpf = input('Digite o CPF do funcionario: ')

        nome = input('Digite o nome do funcionário: ')
        endereco = input('Digite o endereço do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
        
        while True:
            cod_setor = int(input('Digite o código do setor: '))

            setor = repos.SetoresRepository.select_by_cod_setor(cod_setor)

            if setor == None:
                print('Setor inexistente! Por favor tente novamente!')
            else:
                break

        inserted = repos.FuncionariosRepository.insert(
            cpf=cpf,
            nome=nome,
            endereco=endereco,
            salario=salario,
            cod_setor=cod_setor
        )

        if inserted:
            print('Funcionário cadastrado com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar o funcionário! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def insert_professor():
    while True:
        print('Cadastrar professor')
        cpf = input('Digite o CPF do professor: ')

        while len(cpf) != 11:
            print('CPF inválido! Tente novamente')
            cpf = input('Digite o CPF do professor: ')

        nome = input('Digite o nome do professor: ')
        telefone = input('Digite o telefone do professor: ') 
        endereco = input('Digite o endereço do professor: ')
        data_contratacao = input('Digite a data de contratação do professor: ')
        salario = float(input('Digite o salário do professor: '))
        ativo = input('Digite se é ativo (0 inativo, 1 ativo): ')

        if ativo == '0':
            ativo = False
        else:
            ativo = True

        while True:
            cod_curso = int(input('Digite o código do curso: '))

            curso = repos.CursosRepository.select_by_cod_curso(cod_curso)

            if curso == None:
                print('Curso inexistente! Por favor tente novamente!')
            else:
                break

        inserted = repos.ProfessoresRepository.insert(
            cpf=cpf,
            nome=nome,
            telefone=telefone,
            endereco=endereco,
            data_contratacao=data_contratacao,
            salario=salario,
            ativo=ativo,
            cod_curso=cod_curso
        )

        if inserted:
            print('Professor cadastrado com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar o professor! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def insert_aluno():
    while True:
        print('Cadastrar aluno')
        cpf = input('Digite o CPF do aluno: ')

        while len(cpf) != 11:
            print('CPF inválido! Tente novamente')
            cpf = input('Digite o CPF do aluno: ')

        nome = input('Digite o nome do aluno: ')
        telefone = input('Digite o telefone do aluno: ') 
        endereco = input('Digite o endereço do aluno: ')
        ativo = input('Digite se é ativo (0 inativo, 1 ativo): ')

        if ativo == '0':
            ativo = False
        else:
            ativo = True

        inserted = repos.AlunosRepository.insert(
            cpf=cpf,
            nome=nome,
            telefone=telefone,
            endereco=endereco,
            ativo=ativo
        )

        if inserted:
            print('Aluno cadastrado com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar o aluno! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def insert_disciplina():
    print('Cadastrar disciplina')
    input()


def inscrever_aluno():
    print('Inscrever aluno em uma disciplina')
    input()


def lancar_nota():
    print('Lançar nota')
    input()
