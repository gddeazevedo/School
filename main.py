import sys
import os
from school.repositories.setores_repository import SetoresRepository
from school.repositories.funcionarios_repository import FuncionariosRepository


def main():
    commands = {
        'migrate up': 'alembic upgrade head',
        'migrate down': 'alembic downgrade -1',
        'generate migration': 'alembic revision -m '
    }
    try:
        if len(sys.argv) > 2:
            command_key = f'{sys.argv[1]} {sys.argv[2]}'
            command = commands.get(command_key)
            if command_key[0] == 'g':
                print(command + f'"{sys.argv[3]}"')
                os.system(command + f'"{sys.argv[3]}"')
            else:
                os.system(command)
        else:
            print('Running CLI')
            # SetoresRepository.insert('Setor1')
            FuncionariosRepository.insert(
                cpf='11111111111',
                nome='Funcionario 1',
                endereco='Rua Legal numero 42',
                salario=1234.59,
                cod_setor=3
            )
            print(SetoresRepository.select_all())
            print(FuncionariosRepository.select_all())

    except Exception as e:
        print('Invalid command')
        print(e)


if __name__ == '__main__':
    main()
