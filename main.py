import sys
import os
from school.repositories.setores_repository import SetoresRepository


def main():
    commands = {
        'migrate up': 'alembic upgrade head',
        'migrate down': 'alembic downgrade -1'
    }
    try:
        if len(sys.argv) > 2:
            command_key = f'{sys.argv[1]} {sys.argv[2]}'
            command = commands.get(command_key)
            os.system(command)
        else:
            print('Running CLI')
    except Exception as e:
        print('Invalid command')
        print(e)


if __name__ == '__main__':
    main()
