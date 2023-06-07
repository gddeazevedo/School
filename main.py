import sys
import os
from school.cli.cli import cli


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
            cli()

    except Exception as e:
        print('Invalid command')
        print(e)


if __name__ == '__main__':
    main()
