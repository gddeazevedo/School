import os
from .. import repositories as repos


def turma_com_mais_alunos():
    print('Turma com mais alunos')
    input()


def professores_ativos_por_curso():
    print('Quantidade de professores ativos por curso')
    input()


def media_salarial():
    print(' Média salarial por curso')
    input()


def folha_mensal_por_departamento():
    print('Folha mensal de cada departamento (ordem descrescente)')
    input()


def media_notas():
    print('Média  final das notas por disciplina de um determinado professor')
    input()


def qtd_curso_por_prof():
    print('Quantidade de cursos que um determinado professor trabalha')
    input()


def professor_mais_antigos():
    print('Professor mais antigo da instituição')
    input()


def alunos_por_curso():
    print('Número total de alunos por curso')
    input()


def aprovados_reprovados():
    print('Disciplinas com mais aprovados e reprovados em um determinado período')
    input()


def render_other_options_menu():
    print('Mais opções')

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
            print('0) Voltar')
            print('1) Turmas com mais alunos')
            print('2) Quantidade de professores ativos por curso')
            print('3) Média salarial por curso')
            print('4) Folha mensal de cada departamento (ordem descrescente)')
            print('5) Média final das notas por disciplina de um determinado professor')
            print('6) Quantidade de cursos que um determinado professor trabalha')
            print('7) Professor mais antigo da instituição')
            print('8) Número total de alunos por curso')
            print('9) Disciplinas com mais aprovados e reprovados em um determinado período')

            option = input('Escolha uma opção para continuar: ')

            os.system('clear')
            eval(options[option])
            os.system('clear')
        except:
            return
