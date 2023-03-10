/* 
    Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02,
    e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro. */

WITH tabela AS (
    SELECT esto.cdpro, nmpro, COUNT(nmpro) AS contagem
    FROM tbestoqueproduto AS esto

    LEFT JOIN tbvendas AS vend
        ON esto.cdpro = vend.cdpro

    WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02' AND vend.status = 'Concluído'
    GROUP BY nmpro
    )

SELECT cdpro, nmpro
FROM tabela

WHERE contagem = (SELECT max(contagem) FROM tabela)