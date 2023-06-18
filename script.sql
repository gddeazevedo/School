CREATE DATABASE IF NOT EXISTS school;

USE school;

CREATE TABLE IF NOT EXISTS setores (
    cod_setor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionarios (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    salario FLOAT NOT NULL,
    cod_setor INT NOT NULL,
    CONSTRAINT cod_setor_fk FOREIGN KEY (cod_setor) REFERENCES setores(cod_setor) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cursos (
    cod_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    ano_inicio DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS professores (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    data_contratacao DATETIME NOT NULL,
    salario FLOAT NOT NULL,
    ativo BOOLEAN NOT NULL,
    cod_curso INT NOT NULL,
    CONSTRAINT cod_curso_fk1 FOREIGN KEY (cod_curso) REFERENCES cursos(cod_curso) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS alunos (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    ativo BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS disciplinas (
    cod_disciplina INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf_professor VARCHAR(11) NOT NULL,
    CONSTRAINT cpf_professor_fk FOREIGN KEY (cpf_professor) REFERENCES professores(cpf) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cursos_disciplinas (
    cod_curso INT NOT NULL,
    cod_disciplina INT NOT NULL,
    CONSTRAINT cod_curso_fk2 FOREIGN KEY (cod_curso) REFERENCES cursos(cod_curso) ON DELETE CASCADE,
    CONSTRAINT cod_disciplina_fk1 FOREIGN KEY (cod_disciplina) REFERENCES disciplinas(cod_disciplina) ON DELETE CASCADE,
    PRIMARY KEY (cod_curso, cod_disciplina)
);

CREATE TABLE IF NOT EXISTS inscritos (
    cod_disciplina INT NOT NULL,
    cpf_aluno VARCHAR(11) NOT NULL,
    nota FLOAT NOT NULL DEFAULT 0,
    vez INT NOT NULL DEFAULT 1,
    CONSTRAINT cod_disciplina_fk2 FOREIGN KEY (cod_disciplina) REFERENCES disciplinas(cod_disciplina) ON DELETE CASCADE,
    CONSTRAINT cpf_aluno_fk FOREIGN KEY (cpf_aluno) REFERENCES alunos(cpf) ON DELETE CASCADE,
    PRIMARY KEY (cod_disciplina, cpf_aluno)
);


DELIMITER $

CREATE TRIGGER tgr_inativar_aluno AFTER UPDATE
ON inscritos
FOR EACH ROW
BEGIN
    IF new.vez > 3 THEN
        UPDATE alunos SET ativo = FALSE;
    END IF;
END$

DELIMITER ;