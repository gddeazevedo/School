# Aplicação que manipula um sistema de uma escola

## Para rodar o banco de dados

```bash
docker compose up -d
```

## Para desligar o banco

```bash
docker compose down
```

## Para instalar as dependências e rodar o programa

```bash
python -m venv env
source ./env/bin/active
pip install -r requirements.txt
python main.py
```

## Para criar migrações

```bash
alembic revision -m "nome da migração"
```
