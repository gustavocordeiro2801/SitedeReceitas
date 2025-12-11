import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Pegar uma categoria que tem posts
cursor.execute("SELECT DISTINCT category_id FROM blog_post_categorias LIMIT 1")
categoria_com_posts = cursor.fetchone()

if categoria_com_posts:
    categoria_id = categoria_com_posts[0]
    
    print("\n" + "=" * 100)
    print(f"QUERY 4: Listar todos os posts da categoria ID {categoria_id}")
    print("=" * 100)
    
    query = f"""SELECT 
    blog_post.*
FROM blog_post
INNER JOIN blog_post_categorias ON blog_post.id = blog_post_categorias.post_id
WHERE blog_post_categorias.category_id = {categoria_id};"""
    
    print("\nSQL:")
    print(query)
    print("\n" + "-" * 100)
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Pegar nomes das colunas
    column_names = [description[0] for description in cursor.description]
    
    print("\nRESULTADOS:")
    print("\n" + " | ".join(column_names))
    print("-" * 100)
    
    for row in results:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3][:50] if row[3] else 'NULL'}... | ...")
    
    print(f"\nTotal de registros: {len(results)}\n")
else:
    print("\nNenhuma categoria associada a posts encontrada.\n")

conn.close()
