/*  
    Apresente a query para listar a quantidade de livros publicada por cada autor. 
    Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
    Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria). */

SELECT nome, codautor, nascimento, count(publicacao) as quantidade
FROM autor

LEFT JOIN livro
	ON codautor = autor

group by nome
ORDER by nome