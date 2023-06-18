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

        while True:
            cod_curso = int(input('Digite o código do curso: '))

            curso = repos.CursosRepository.select_by_cod_curso(cod_curso)

            if curso == None:
                print('Curso inexistente! Por favor tente novamente!')
            else:
                break


        inserted = repos.AlunosRepository.insert(
            cpf=cpf,
            nome=nome,
            telefone=telefone,
            endereco=endereco,
            ativo=ativo,
            cod_curso=cod_curso
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
    while True:
        print('Cadastrar disciplina')

        cod_disciplina = int(input('Digite o código da disciplina: '))
        nome = input('Digite o nome da disciplina: ')

        cpf_professor = None

        while True:
            cpf_professor = input('Digite o CPF do professor: ')

            if len(cpf_professor) != 11:
                print('CPF inválido! Tente novamente')
                continue

            professor = repos.ProfessoresRepository.select_by_cpf(cpf_professor)

            if professor == None:
                print('Professor inexistente! Por favor tente novamente!')
            else:
                break

        inserted = repos.DisciplinasRepository.insert(
            cod_disciplina=cod_disciplina,
            cpf_professor=cpf_professor,
            nome=nome
        )

        if inserted:
            print('Disciplina cadastrada com sucesso!')
            input('Aperte enter para sair!')
            os.system('clear')
            return
        else:
            print('Erro ao cadastrar a disciplina! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')


def inscrever_aluno():
    while True:
        print('Inscrever aluno')

        while True:
            cpf_aluno = input('Digite o CPF do aluno: ')

            if len(cpf_aluno) != 11:
                print('CPF inválido! Tente novamente')
                continue

            aluno = repos.AlunosRepository.select_by_cpf(cpf_aluno)

            if aluno == None:
                print('Aluno inexistente! Por favor tente novamente!')
            else:
                if not aluno.ativo:
                    print('Aluno não está mais ativo!')
                    input('Aperte enter para continuar!')
                    os.system('clear')
                    return
                break

        while True:
            cod_disciplina = int(input('Digite o código da disciplina: '))
            disciplina = repos.DisciplinasRepository.select_by_cod_disciplina(cod_disciplina)

            if disciplina == None:
                print('Disciplina inexistente! Tente novamente')
            else:
                break

        inscrito = repos.InscritosRepository.select_by_cpf_aluno_and_cod_disciplina(
            cpf_aluno=cpf_aluno, cod_disciplina=cod_disciplina
        )

        if inscrito == None:
            if repos.InscritosRepository.insert(cpf_aluno, cod_disciplina, 0.0, 1):
                print('Aluno cadastrado com sucesso!')
                input('Aperte enter para sair')
                return
            else:
                print('Erro ao inscrever o aluno! Tente novamente!')
                input('Aperte enter para tentar de novo!')
                os.system('clear')
        else:
            if inscrito.vez < 3:
                repos.InscritosRepository.update(
                    cpf_aluno=cpf_aluno,
                    cod_disciplina=cod_disciplina,
                    vez=inscrito.vez + 1
                )
                print('Aluno já estava inscrito e foi inscrito novamente!')
                input('Aperte enter para sair')
                return
            else:
                if aluno.ativo:
                    repos.AlunosRepository.update(cpf_aluno, ativo=False)

                print('Aluno não está mais ativo!')
                input('Aperte enter para continuar!')
                os.system('clear')
                return


def cancelar_inscricao():
    while True:
        print('Cancelar inscrição')

        while True:
            cod_disciplina = int(input('Digite o código da disciplina: '))
            disciplina = repos.DisciplinasRepository.select_by_cod_disciplina(cod_disciplina)

            if disciplina == None:
                print('Disciplina inexistente! Tente novamente')
            else:
                break

        while True:
            cpf_aluno = input('Digite o CPF do aluno: ')

            if len(cpf_aluno) != 11:
                print('CPF inválido! Tente novamente')
                continue

            aluno = repos.AlunosRepository.select_by_cpf(cpf_aluno)

            if aluno == None:
                print('Aluno inexistente! Por favor tente novamente!')
            else:
                if not aluno.ativo:
                    print('Aluno não está mais ativo!')
                    input('Aperte enter para continuar!')
                    os.system('clear')
                    return
                break

        inscrito = repos.InscritosRepository.select_by_cpf_aluno_and_cod_disciplina(
            cpf_aluno=cpf_aluno, cod_disciplina=cod_disciplina
        )

        if inscrito == None:
            input('Este aluno não está inscrito nesta disciplina! Por favor, tente novamente!')
            os.system('clear')
            continue

        if repos.InscritosRepository.delete(cpf_aluno, cod_disciplina):
            print('Aluno removido da disciplina com sucesso!')
            input('Aperte enter para voltar! ')
            return
        else:
            print('Erro ao remover o aluno da disciplina!')
            input('Aperte enter para tentar de novo!')


def lancar_nota():
    while True:
        print('Lançar nota')

        while True:
            cpf_aluno = input('Digite o CPF do aluno: ')

            if len(cpf_aluno) != 11:
                print('CPF inválido! Tente novamente')
                continue

            aluno = repos.AlunosRepository.select_by_cpf(cpf_aluno)

            if aluno == None:
                print('Aluno inexistente! Por favor tente novamente!')
            else:
                if not aluno.ativo:
                    print('Aluno não está mais ativo!')
                    input('Aperte enter para continuar!')
                    os.system('clear')
                    return
                break

        while True:
            cod_disciplina = int(input('Digite o código da disciplina: '))
            disciplina = repos.DisciplinasRepository.select_by_cod_disciplina(cod_disciplina)

            if disciplina == None:
                print('Disciplina inexistente! Tente novamente')
            else:
                break

        nota = float(input('Digite a nota: '))

        while nota < 0 or nota > 10:
            print('Nota inválida! Tente novamente!')
            nota = float(input('Digite a nota: '))

        inscrito = repos.InscritosRepository.select_by_cpf_aluno_and_cod_disciplina(
            cpf_aluno=cpf_aluno, cod_disciplina=cod_disciplina
        )

        if inscrito == None:
            input('Este aluno não está inscrito nesta disciplina! Por favor, tente novamente!')
            os.system('clear')
            continue

        if repos.InscritosRepository.update(cpf_aluno, cod_disciplina, nota=nota):
            print('Nota lançada com sucesso')
            input('Aperte enter para sair')
            return
        else:
            print('Erro ao lançar a nota! Tente novamente!')
            input('Aperte enter para tentar de novo!')
            os.system('clear')
