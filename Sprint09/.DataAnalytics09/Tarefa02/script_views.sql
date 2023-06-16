CREATE VIEW dim_cliente AS
    SELECT *
    FROM tb_clientea;

CREATE VIEW dim_carro AS
    SELECT *
    FROM tb_carro;

CREATE VIEW dim_combustivel AS
    SELECT *
    FROM tb_combustivel;

CREATE VIEW dim_vendedor AS
    SELECT *
    FROM tb_vendedor;

CREATE VIEW dim_locacao AS
    SELECT idLocacao,
        dataLocacao,
        horaLocacao,
        qtdDiaria,
        vlrDiaria,
        dataEntrega,
        horaEntrega
    FROM tb_locacao;

CREATE VIEW fato_locacao AS
    SELECT idLocacao,
        idCliente,
        idCarro,
        kmCarro,
        idVendedor
    FROM tb_locacao;



