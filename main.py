import sys
import os
from school.cli import cli, seed


def main():
    commands = {
        'migrate up': 'alembic upgrade head',
        'migrate down': 'alembic downgrade base',
        'generate migration': 'alembic revision -m ',
        'seed': seed.seed_all_db,
        'start': cli.start
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
            commands[sys.argv[1]]()
    except Exception as e:
        print('Invalid command')
        print(e)


if __name__ == '__main__':
    main()
