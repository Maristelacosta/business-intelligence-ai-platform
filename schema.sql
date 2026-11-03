CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ativos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE chamados (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    descricao TEXT,
    prioridade VARCHAR(20),
    status VARCHAR(20),
    data_abertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
