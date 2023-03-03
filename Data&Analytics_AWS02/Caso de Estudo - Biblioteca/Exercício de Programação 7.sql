/*  
    Apresente a query para listar o nome dos autores com nenhuma publicação. 
    Apresentá-los em ordem crescente. */

SELECT nome
from autor

LEFT JOIN livro
	ON codautor = autor
    
WHERE publicacao IS NULL
ORDER BY nome