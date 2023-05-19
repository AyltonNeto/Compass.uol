/* 
    Apresente a query para listar o autor com maior número de livros publicados. 
    O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. */

SELECT codautor, nome, COUNT(publicacao) as quantidade_publicacoes
FROM autor
    
LEFT JOIN livro
	ON codautor = autor

GROUP by nome
ORDER by quantidade_publicacoes DESC
LIMIT 1