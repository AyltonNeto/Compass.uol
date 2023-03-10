/*
    Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas 
    vendas estejam com o status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd. */

WITH tabela AS (
    SELECT vendedor.cdvdd, nmvdd, COUNT(cdven) AS contagem, status
	FROM tbvendedor AS vendedor
    
	LEFT JOIN tbvendas AS vendas
        ON vendedor.cdvdd = vendas.cdvdd

    WHERE status = 'Concluído'
    GROUP BY nmvdd, status
    )

SELECT tabela.cdvdd, nmvdd
FROM tabela

WHERE contagem = (SELECT max(contagem) FROM tabela)


