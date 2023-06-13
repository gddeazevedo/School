# Aplicação que manipula um sistema de uma escola

## Para rodar o banco de dados

```bash
docker compose up -d
```

## Para acessar o banco

```bash
docker exec -it school_db mysql -u root -p
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
python main.py generate migration "nome da migração"
```

## Migrate Up

```bash
python main.py migrate up
```

## Migrate Down

```bash
python main.py migrate down
```
