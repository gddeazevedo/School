CREATE DATABASE IF NOT EXISTS school;

USE school;

CREATE DATABASE IF NOT EXISTS setores (
    cod_setor INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    salario FLOAT NOT NULL,
    cod_setor INT NOT NULL,
    CONSTRAINT cod_setor_fk FOREIGN KEY (cod_setor) REFERENCES setores(cod_setor)
);

CREATE TABLE IF NOT EXISTS cursos (
    cod_curso INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano_inicio DATETIME NOT NULL
);
