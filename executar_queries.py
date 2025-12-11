import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def print_results(query_name, query_sql):
    """Executa e imprime os resultados de uma query"""
    print("\n" + "=" * 100)
    print(f"{query_name}")
    print("=" * 100)
    print(f"SQL:\n{query_sql}")
    print("-" * 100)
    
    cursor.execute(query_sql)
    results = cursor.fetchall()
    
    # Pegar nomes das colunas
    column_names = [description[0] for description in cursor.description]
    print("\nResultados:")
    print(" | ".join(column_names))
    print("-" * 100)
    
    if results:
        for row in results:
            # Limitar o tamanho dos campos para melhor visualização
            formatted_row = []
            for value in row:
                str_value = str(value) if value is not None else "NULL"
                # Truncar textos muito longos
                if len(str_value) > 50:
                    str_value = str_value[:50] + "..."
                formatted_row.append(str_value)
            print(" | ".join(formatted_row))
        print(f"\nTotal de registros: {len(results)}")
    else:
        print("Nenhum registro encontrado.")
    print("\n")

# QUERY 1
query1 = """SELECT * FROM blog_post
ORDER BY data_postagem DESC;"""
print_results("QUERY 1: Listar todos os posts ordenados por data de postagem", query1)

# QUERY 2 - Comentários de um post específico
# Primeiro, vamos pegar um post que tem comentários
cursor.execute("SELECT DISTINCT post_id FROM blog_comment LIMIT 1")
post_com_comentario = cursor.fetchone()
if post_com_comentario:
    post_id = post_com_comentario[0]
    query2 = f"""SELECT * FROM blog_comment
WHERE post_id = {post_id}
ORDER BY data_postagem DESC;"""
    print_results(f"QUERY 2: Comentários do post ID {post_id}", query2)
else:
    print("\nQUERY 2: Nenhum comentário encontrado no banco de dados.\n")

# QUERY 3 - Comentários com título do post
query3 = """SELECT 
    blog_comment.id,
    blog_comment.texto,
    blog_comment.data_postagem AS data_comentario,
    blog_post.titulo AS titulo_post,
    blog_post.data_postagem AS data_post
FROM blog_comment
INNER JOIN blog_post ON blog_comment.post_id = blog_post.id
ORDER BY blog_comment.data_postagem DESC;"""
print_results("QUERY 3: Comentários com título do post e data de postagem", query3)

# QUERY 4 - Posts de uma categoria específica
cursor.execute("SELECT DISTINCT category_id FROM blog_post_categorias LIMIT 1")
categoria_com_posts = cursor.fetchone()
if categoria_com_posts:
    categoria_id = categoria_com_posts[0]
    query4 = f"""SELECT 
    blog_post.*
FROM blog_post
INNER JOIN blog_post_categorias ON blog_post.id = blog_post_categorias.post_id
WHERE blog_post_categorias.category_id = {categoria_id};"""
    print_results(f"QUERY 4: Posts da categoria ID {categoria_id}", query4)
else:
    print("\nQUERY 4: Nenhuma categoria associada a posts encontrada.\n")

# QUERY 5 - Categorias com 2 ou mais posts
query5 = """SELECT 
    blog_category.id,
    blog_category.nome,
    blog_category.descricao,
    COUNT(blog_post_categorias.post_id) AS total_posts
FROM blog_category
INNER JOIN blog_post_categorias ON blog_category.id = blog_post_categorias.category_id
GROUP BY blog_category.id, blog_category.nome, blog_category.descricao
HAVING COUNT(blog_post_categorias.post_id) >= 2
ORDER BY total_posts DESC;"""
print_results("QUERY 5: Categorias com 2 ou mais posts (COUNT, GROUP BY, HAVING)", query5)

conn.close()
print("=" * 100)
print("Todas as queries foram executadas com sucesso!")
print("=" * 100)
