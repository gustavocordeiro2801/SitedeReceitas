-- Exercícios SQL - Segunda Entrega de Laboratório
-- Banco de dados: db.sqlite3

-- Query 1: Listar todos os posts ordenados por data de postagem (mais recentes primeiro)
SELECT * FROM blog_post
ORDER BY data_postagem DESC;

-- Query 2: Listar todos os comentários de um post específico
-- (Substitua o '1' pelo ID do post que você quer consultar)
SELECT * FROM blog_comment
WHERE post_id = 1
ORDER BY data_postagem DESC;

-- Query 3: Listar comentários com título do post e data de postagem do post
SELECT 
    blog_comment.id,
    blog_comment.texto,
    blog_comment.data_postagem AS data_comentario,
    blog_post.titulo AS titulo_post,
    blog_post.data_postagem AS data_post
FROM blog_comment
INNER JOIN blog_post ON blog_comment.post_id = blog_post.id
ORDER BY blog_comment.data_postagem DESC;

-- Query 4: Listar todos os posts de uma categoria específica
-- (Substitua o '1' pelo ID da categoria que você quer consultar)
SELECT 
    blog_post.*
FROM blog_post
INNER JOIN blog_post_categorias ON blog_post.id = blog_post_categorias.post_id
WHERE blog_post_categorias.category_id = 1;

-- Query 5: Listar categorias com 2 ou mais posts (usando COUNT, GROUP BY e HAVING)
SELECT 
    blog_category.id,
    blog_category.nome,
    blog_category.descricao,
    COUNT(blog_post_categorias.post_id) AS total_posts
FROM blog_category
INNER JOIN blog_post_categorias ON blog_category.id = blog_post_categorias.category_id
GROUP BY blog_category.id, blog_category.nome, blog_category.descricao
HAVING COUNT(blog_post_categorias.post_id) >= 2
ORDER BY total_posts DESC;
