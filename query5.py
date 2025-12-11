import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n" + "=" * 100)
print("QUERY 5: Listar categorias com 2 ou mais posts (usando COUNT, GROUP BY e HAVING)")
print("=" * 100)

query = """SELECT 
    blog_category.id,
    blog_category.nome,
    blog_category.descricao,
    COUNT(blog_post_categorias.post_id) AS total_posts
FROM blog_category
INNER JOIN blog_post_categorias ON blog_category.id = blog_post_categorias.category_id
GROUP BY blog_category.id, blog_category.nome, blog_category.descricao
HAVING COUNT(blog_post_categorias.post_id) >= 2
ORDER BY total_posts DESC;"""

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

if results:
    for row in results:
        descricao = row[2][:50] + "..." if row[2] and len(row[2]) > 50 else row[2]
        print(f"{row[0]} | {row[1]} | {descricao} | {row[3]}")
    
    print(f"\nTotal de registros: {len(results)}\n")
else:
    print("\nNenhuma categoria com 2 ou mais posts encontrada.\n")

conn.close()
