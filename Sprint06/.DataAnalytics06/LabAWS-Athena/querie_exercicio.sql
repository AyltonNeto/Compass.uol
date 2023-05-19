--Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

WITH dados_decada AS (
    SELECT 
        CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s') AS decada, nome, SUM(total) AS total_por_nome,
        ROW_NUMBER() OVER (PARTITION BY CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s') ORDER BY SUM(total) DESC) AS rank
    FROM nomes
    
    WHERE
        CAST(SUBSTRING(CAST(ano AS VARCHAR), 1, 3) || '0' AS INT) <= EXTRACT(YEAR FROM current_date)
    GROUP BY
        CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s'), nome
)

SELECT decada, nome, total_por_nome
FROM dados_decada

WHERE rank <= 3
ORDER BY decada, total_por_nome DESC

