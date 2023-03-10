/*
    Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor 
    com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado 
    devem ser cddep, nmdep, dtnasc e valor_total_vendas.

    Observação: Apenas vendas com status concluído. */

SELECT cddep, nmdep, dtnasc, sum(qtd * vrunt) AS valor_total_vendas
FROM tbdependente AS dependente

LEFT JOIN tbvendedor AS vendedor
	ON dependente.cdvdd = vendedor.cdvdd

LEFT JOIN tbvendas AS vendas
	ON dependente.cdvdd = vendas.cdvdd
    
WHERE status = 'Concluído'
GROUP BY cddep
ORDER BY valor_total_vendas
LIMIT 1

