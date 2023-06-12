import faker
import random
import sqlalchemy as sa
from .. import repositories as repos
from ..config.db_connection_handler import DBConnectionHandler


SEED = 100

fake = faker.Faker()


def seed_setores():
    for i in range(SEED):
        cod_setor = i + 1
        nome = fake.company()
        repos.SetoresRepository.insert(cod_setor=cod_setor, nome=nome)


def seed_funcionarios():
    for i in range(SEED):
        cpf = fake.msisdn()[:11]
        nome = fake.name()
        endereco = fake.address()
        salario = fake.pyfloat(positive=True, right_digits=2, max_value=10_000.00)
        cod_setor = random.randint(1, SEED)

        repos.FuncionariosRepository.insert(cpf, nome, endereco, salario, cod_setor)


def seed_cursos():
    for i in range(SEED):
        cod_curso = i + 1
        nome = fake.company()
        ano_inicio = random.randint(1999, 2020)

        repos.CursosRepository.insert(cod_curso=cod_curso, nome=nome, ano_inicio=ano_inicio)


def seed_professores_and_disciplinas():
    for i in range(SEED):
        cpf = fake.msisdn()[:11]
        nome = fake.name()
        telefone = fake.msisdn()[:11]
        endereco = fake.address()
        data_contratacao = fake.date()
        salario = fake.pyfloat(positive=True, right_digits=2, max_value=10_000.00)
        ativo = fake.pybool()
        cod_curso = random.randint(1, SEED)

        repos.ProfessoresRepository.insert(
            cpf=cpf,
            nome=nome,
            endereco=endereco,
            telefone=telefone,
            data_contratacao=data_contratacao,
            salario=salario,
            ativo=ativo,
            cod_curso=cod_curso
        )

        cod_disciplina = i + 1
        nome = fake.company()

        repos.DisciplinasRepository.insert(
            cod_disciplina=cod_disciplina,
            nome=nome,
            cpf_professor=cpf
        )

def seed_alunos():
    for i in range(SEED):
        cpf = fake.msisdn()[:11]
        nome = fake.name()
        telefone = fake.msisdn()[:11]
        endereco = fake.address()
        ativo = fake.pybool()

        try:
            repos.AlunosRepository.insert(
                cpf=cpf,
                nome=nome,
                telefone=telefone,
                endereco=endereco,
                ativo=ativo
            )
        except Exception as e:
            print(e)


def seed_all_db():
    print('Deleting...')

    db = DBConnectionHandler()
    
    databases = ['cursos', 'alunos', 'professores', 'funcionarios', 'setores', 'disciplinas']
    for database in databases:
        query = sa.text(f'DELETE FROM {database};')
        print(query)
        conn = db.engine.connect()
        conn.execute(query)
        conn.commit()

    print('Seeding...')

    seed_cursos()
    seed_professores_and_disciplinas()
    seed_setores()
    seed_funcionarios()
    seed_alunos()

    print('Done')
