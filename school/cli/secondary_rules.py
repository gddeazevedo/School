import os
import sqlalchemy as sa
from tabulate import tabulate
from .. import repositories as repos
from ..config.db_connection_handler import DBConnectionHandler


def print_table(table: list[tuple[int | bool | str | float]]):
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    input('Aperte enter para voltar')


def turma_com_mais_alunos():
    '''
    select nome, count(cpf_aluno)
    from disciplinas as d inner join inscritos as i
    on i.cod_disciplina = d.cod_disciplina
    group by nome having count(cpf_aluno) >= all (
        select count(cpf_aluno)
        from disciplinas inner join inscritos
        on inscritos.cod_disciplina = disciplinas.cod_disciplina
        group by nome
    );
    '''
    while True:
        print('Turma com mais alunos')
        rows = repos.DisciplinasRepository.get_with_mais_inscritos()
        table = [('Nome Disciplina', 'Quantidade de alunos')]
        table.extend(rows)
        print_table(table)
        return


def professores_ativos_por_curso():
    '''
    select cursos.cod_curso as cod_curso, cursos.nome as nome_curso, count(professores.cpf) as qtd_professores
    from cursos inner join professores on professores.cod_curso = cursos.cod_curso
    where professores.ativo = 1
    group by cursos.cod_curso, cursos.nome
    order by cursos.cod_curso;
    '''
    while True:
        print('Quantidade de professores ativos por curso')
        rows = repos.CursosRepository.get_qtd_professores_ativos_by_curso()
        table = [('Cod Curso', 'Nome Curso', 'Quantidade de professores')]
        table.extend(rows)
        print_table(table)
        return


def media_salarial():
    '''
    select cursos.cod_curso, cursos.nome, avg(professores.salario)
    from cursos inner join professores on cursos.cod_curso = professores.cod_curso
    group by cursos.cod_curso, cursos.nome
    order by cursos.cod_curso;
    '''
    while True:
        print('Média salarial por curso')
        rows = repos.CursosRepository.get_media_salario_by_curso()
        table = [('Cod Curso', 'Nome Curso', 'Média salarial')]
        table.extend(rows)
        print_table(table)
        return


def folha_mensal_por_departamento():
    '''
    select setores.cod_setor, setores.nome, sum(funcionarios.salario)
    from setores inner join funcionarios on setores.cod_setor = funcionarios.cod_setor
    group by setores.cod_setor, setores.nome order by sum(funcionarios.salario) desc;
    '''
    while True:
        print('Folha mensal de cada departamento (ordem descrescente)')
        rows = repos.SetoresRepository.get_folha_pagamento_by_setor()
        table = [('Cod Setor', 'Nome Setor', 'Folha de Pagamento Mensal')]
        table.extend(rows)
        print_table(table)
        return


def media_notas():
    '''
    create temporary table t (
        select professores.nome as nome_p, cod_disciplina, disciplinas.nome as nome_d
        from professores inner join disciplinas
        on cpf = cpf_professor
        where cpf = :cpf
    );

    select nome_p, nome_d, avg(nota) as media
    from t inner join inscritos
    on t.cod_disciplina = inscritos.cod_disciplina
    group by nome_p, nome_d;
    '''
    while True:
        print('Média final das notas por disciplina de um determinado professor')
        cpf_professor = input('Digite o CPF do professor: ')
        rows = repos.ProfessoresRepository.get_media_notas(cpf_professor)
        table = [('Nome Profesor', 'Nome Disciplina', 'Média das notas')]
        table.extend(rows)
        print_table(table)
        return


def qtd_curso_por_prof():
    '''
    select professores.nome, professores.cpf, count(cod_curso) as qtd_cursos
    from professores inner join disciplinas on professores.cpf = disciplinas.cpf_professor
    inner join cursos_disciplinas
    group by professores.nome, professores.cpf
    order by qtd_cursos, professor.nome;
    '''
    while True:
        print('Quantidade de cursos que cada professor trabalha')
        rows = repos.ProfessoresRepository.get_qtd_cursos_by_professor()
        table = [('CPF Professor', 'Nome Professor', 'Quantidade de Cursos')]
        table.extend(rows)
        print_table(table)
        return


def professor_mais_antigos():
    '''
    select cpf, nome, data_contratacao from professores as p1
    where data_contratacao < all (
        select data_contratacao from professores as p2 where p1.cpf <> p2.cpf
    );
    '''
    while True:
        print('Professor mais antigo da instituição')
        row = repos.ProfessoresRepository.get_professor_mais_antigo()
        table = [('CPF', 'Nome', 'Data Contratação')]
        table.extend(row)
        print_table(table)
        return


def alunos_por_curso():
    '''
    select cursos.cod_curso, cursos.nome, count(alunos.cpf)
    from cursos inner join alunos on cursos.cod_curso = alunos.cod_curso
    group by cursos.cod_curso, cursos.nome
    order by count(alunos.cpf);
    '''
    while True:
        print('Número total de alunos por curso')
        rows = repos.CursosRepository.get_qtd_alunos_by_curso()
        table = [('Cod Curso', 'Nome Curso', 'Quantidade de Alunos')]
        table.extend(rows)
        print_table(table)
        return


def aprovados_reprovados():
    print('Disciplinas com mais aprovados e reprovados em um determinado período')
    input()


def render_other_options_menu():
    options = {
        '0': 'raise',
        '1': 'turma_com_mais_alunos()',
        '2': 'professores_ativos_por_curso()',
        '3': 'media_salarial()',
        '4': 'folha_mensal_por_departamento()',
        '5': 'media_notas()',
        '6': 'qtd_curso_por_prof()',
        '7': 'professor_mais_antigos()',
        '8': 'alunos_por_curso()',
        '9': 'aprovados_reprovados()'
    }

    while True:
        try:
            print('Mais opções')
            print('0) Voltar')
            print('1) Turmas com mais alunos')
            print('2) Quantidade de professores ativos por curso')
            print('3) Média salarial por curso')
            print('4) Folha mensal de cada departamento (ordem descrescente)')
            print('5) Média final das notas por disciplina de um determinado professor')
            print('6) Quantidade de cursos que cada professor trabalha')
            print('7) Professor mais antigo da instituição')
            print('8) Número total de alunos por curso')
            print('9) Disciplinas com mais aprovados e reprovados em um determinado período')

            option = input('Escolha uma opção para continuar: ')

            os.system('clear')
            eval(options[option])
            os.system('clear')
        except Exception as e:
            os.system('clear')
            return
