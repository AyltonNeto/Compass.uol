-- 1ª Parte | Renomear da Tabela Locacao --
ALTER TABLE tb_locacao
RENAME TO tb_locacaoOriginal;

-- 2ª Parte | Criação das Tabelas --
CREATE TABLE tb_cliente (
    idCliente       INT PRIMARY KEY,
    nomeCliente     VARCHAR,
    cidadeCliente   VARCHAR,
    estadoCliente   VARCHAR,
    paisCliente     VARCHAR
);

CREATE TABLE tb_combustivel (
    idCombustivel   INT PRIMARY KEY,
    tipoCombustivel VARCHAR
);

CREATE TABLE tb_carro (
    idCarro         INT PRIMARY KEY,
    chassiCarro     VARCHAR,
    marcaCarro      VARCHAR,
    modeloCarro     VARCHAR,
    anoCarro        INT,
    idCombustivel   INT,
    FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

CREATE TABLE tb_vendedor (
    idVendedor      INT PRIMARY KEY,
    nomeVendedor    VARCHAR,
    sexoVendedor    INT,
    estadoVendedor  VARCHAR
);

CREATE TABLE tb_locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    kmCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES tb_cliente (idCliente),
    FOREIGN KEY (idCarro) REFERENCES tb_carro (idCarro),
    FOREIGN KEY (idVendedor) REFERENCES tb_vendedor (idVendedor)
);

-- 3ª Parte | Transferir Dados --
INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacaoOriginal;

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacaoOriginal;

INSERT INTO tb_carro (idCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacaoOriginal;

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacaoOriginal;

INSERT INTO tb_locacao (idLocacao, idCliente, idCarro, kmCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCliente, idCarro, kmCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacaoOriginal;