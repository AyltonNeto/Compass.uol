/*
    A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
    O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

    Com base em tais informações, calcule a comissão de todos os vendedores, 
    considerando todas as vendas armazenadas na base de dados com status concluído.

    As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. 
    O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal. */

WITH tabela AS (
    SELECT nmvdd, (perccomissao), nmpro, vendas.status,
  	sum(qtd * vrunt) AS valor_total_vendas
    FROM tbvendedor AS vendedor

    left JOIN tbvendas AS vendas
        ON vendedor.cdvdd = vendas.cdvdd

    WHERE status = 'Concluído'
    GROUP BY nmvdd
	)

SELECT nmvdd AS vendedor, valor_total_vendas, round(sum(valor_total_vendas * perccomissao/100),2) AS comissao
FROM tabela

GROUP BY nmvdd
ORDER BY comissao DESC