/* 
    Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
    Ordene o resultado pela coluna nome, em ordem crescente. 
    Não podem haver nomes repetidos em seu retorno. */

SELECT DISTINCT(autor.nome)
FROM autor

LEFT JOIN livro
	ON codautor = autor

LEFT JOIN editora
	ON editora = codeditora

LEFT JOIN endereco
	ON endereco = codendereco

WHERE estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')