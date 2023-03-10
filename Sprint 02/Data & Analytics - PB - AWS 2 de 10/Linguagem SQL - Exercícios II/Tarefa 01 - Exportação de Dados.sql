--  1) Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ; (ponto e vírgula) como separador. 
--  Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo: */

SELECT 
	cod as CodLivro, 
    titulo as Titulo,
    codautor as CodAutor,
    autor.nome as NomeAutor,
    valor as Valor,
    codeditora as CodEditora,
    editora.nome as NomeEditora
FROM autor 

LEFT JOIN livro
	ON codautor = autor

LEFT JOIN editora
	on editora = codeditora

ORDER BY valor DESC
LIMIT 10



--  2) Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere | (pipe) como separador. 
--  Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:

SELECT 
	codeditora AS CodEditora,
	nome as NomeEditora,
    COUNT(cod) as QuantidadeLivros
FROM livro

LEFT JOIN editora 
	ON editora = codeditora

GROUP by editora
ORDER by QuantidadeLivros DESC
LIMIT 5


