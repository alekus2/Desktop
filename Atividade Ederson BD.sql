DROP DATABASE IF EXISTS atividade_bd;
CREATE DATABASE atividade_bd;
USE atividade_bd;

-- Criação das tabelas de referência
CREATE TABLE SEXO (
    idSexo INT PRIMARY KEY AUTO_INCREMENT,
    sexo VARCHAR(10) NOT NULL
);

CREATE TABLE SITUACAO_ICMS (
    idSituacao INT PRIMARY KEY AUTO_INCREMENT,
    situacao_icms VARCHAR(25) NOT NULL
);

CREATE TABLE TABELA_PRECO (
    idTabela_preco INT PRIMARY KEY AUTO_INCREMENT,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE REGIME_TRIBUTACAO (
    idRegime INT PRIMARY KEY AUTO_INCREMENT,
    regime_tri VARCHAR(35) NOT NULL
);

CREATE TABLE SIT_CADASTRO (
    idSit_cadastro INT PRIMARY KEY AUTO_INCREMENT,
    sit_cadastro VARCHAR(35) NOT NULL
);

CREATE TABLE MODO_FRETE (
    idFrete INT PRIMARY KEY AUTO_INCREMENT,
    frete VARCHAR(30) NOT NULL
);

-- Criação da tabela CADASTRO_CLIENTE com referências às tabelas de referência
CREATE TABLE CADASTRO_CLIENTE (
    idCliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(80) NOT NULL,
    email_danfe VARCHAR(80) NOT NULL,
    email_cobranca VARCHAR(70) NOT NULL,
    email_loja_virtual VARCHAR(70) NOT NULL,
    fone_comercial VARCHAR(14) NOT NULL,
    ramal VARCHAR(15) NOT NULL,
    fone_residencia VARCHAR(14) NOT NULL,
    fone_celular VARCHAR(14) NOT NULL,
    fax VARCHAR(70),
    cpf VARCHAR(15) NOT NULL,
    rg VARCHAR(13) NOT NULL,
    data_nasc DATE NOT NULL,
    inscri_estadual VARCHAR(60) NOT NULL,
    inscri_suframa VARCHAR(60) NOT NULL,
    transportadora_1 VARCHAR(60) NOT NULL,
    transportadora_2 VARCHAR(60) NOT NULL,
    linha_pef VARCHAR(30) NOT NULL,
    aliquota FLOAT NOT NULL,
    sexo_id INT,
    situacao_icms_id INT,
    preco_id INT,
    regime_tributacao_id INT,
    sit_cadastro_id INT,
    frete_id INT,
    FOREIGN KEY (sexo_id) REFERENCES SEXO(idSexo),
    FOREIGN KEY (situacao_icms_id) REFERENCES SITUACAO_ICMS(idSituacao),
    FOREIGN KEY (preco_id) REFERENCES TABELA_PRECO(idTabela_preco),
    FOREIGN KEY (regime_tributacao_id) REFERENCES REGIME_TRIBUTACAO(idRegime),
    FOREIGN KEY (sit_cadastro_id) REFERENCES SIT_CADASTRO(idSit_cadastro),
    FOREIGN KEY (frete_id) REFERENCES MODO_FRETE(idFrete)
);

-- Inserção de dados nas tabelas de referência
INSERT INTO SEXO (sexo) VALUES ('Masculino'), ('Feminino');
INSERT INTO SITUACAO_ICMS (situacao_icms) VALUES ('Ativo'), ('Inativo');
INSERT INTO TABELA_PRECO (preco) VALUES (100.00), (200.00);
INSERT INTO REGIME_TRIBUTACAO (regime_tri) VALUES ('Simples Nacional'), ('Lucro Presumido');
INSERT INTO SIT_CADASTRO (sit_cadastro) VALUES ('Cadastrado'), ('Não Cadastrado');
INSERT INTO MODO_FRETE (frete) VALUES ('Expressa'), ('Normal');

-- Inserção de dados na tabela CADASTRO_CLIENTE
INSERT INTO CADASTRO_CLIENTE (
    nome, email, email_danfe, email_cobranca, email_loja_virtual, 
    fone_comercial, ramal, fone_residencia, fone_celular, fax, 
    cpf, rg, data_nasc, inscri_estadual, inscri_suframa, 
    transportadora_1, transportadora_2, linha_pef, aliquota, 
    sexo_id, situacao_icms_id, preco_id, regime_tributacao_id, 
    sit_cadastro_id, frete_id
) VALUES (
    'João da Silva', 'joao.silva@example.com', 'danfe.joao@example.com', 
    'cobranca.joao@example.com', 'loja.joao@example.com', 
    '(11) 1234-5678', '123', '(11) 8765-4321', '(11) 91234-5678', 
    '1234-5678', '123.456.789-00', 'MG-12.345.678', '1980-01-01', 
    '123456789012', '123456789012', 'Transportadora A', 
    'Transportadora B', 'Linha A', 18.50, 
    1, 1, 1, 1, 1, 1
);
