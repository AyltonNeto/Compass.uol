/* 
    Apresente a query para listar o autor com maior número de livros publicados. 
    O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. */

SELECT codautor, nome, COUNT(publicacao) as quantidade_publicacoes
FROM autor
    
LEFT JOIN livro
	ON codautor = autor

group by nome
HAVING quantidade_publicacoes = 7 --(Como substituir esse 7 por um comando?)