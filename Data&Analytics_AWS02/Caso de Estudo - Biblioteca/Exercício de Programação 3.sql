/*  
    Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
    O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
    Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente. */

SELECT COUNT(editora) as quantidade, nome, estado, cidade
FROM endereco

LEFT JOIN editora
	on codendereco = endereco

LEFT join livro
	ON codeditora = editora
    
GROUP BY editora
HAVING editora NOTNULL
ORDER by quantidade DESC
LIMIT 5