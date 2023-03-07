/*
    Apresente a query para listar o código e nome cliente com maior gasto na loja. 
    As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última 
    representando o somatório das vendas (concluídas) atribuídas ao cliente. */
    
SELECT cdcli, nmcli, SUM(vrunt*qtd) AS gasto
FROM tbvendas AS vendas

GROUP BY nmcli
ORDER BY gasto DESC
LIMIT 1



-- Outra Opção --

WITH tabela AS (
    SELECT cdcli, nmcli, SUM(vrunt*qtd) AS gasto1
	FROM tbvendas AS vendas

	GROUP BY nmcli
	ORDER BY gasto1 DESC
	)
    
SELECT cdcli, nmcli, max(gasto1) AS gasto
FROM tabela