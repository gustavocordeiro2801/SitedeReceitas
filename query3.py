import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n" + "=" * 100)
print("QUERY 3: Listar comentários com título do post e data de postagem")
print("=" * 100)

query = """SELECT 
    blog_comment.id,
    blog_comment.texto,
    blog_comment.data_postagem AS data_comentario,
    blog_post.titulo AS titulo_post,
    blog_post.data_postagem AS data_post
FROM blog_comment
INNER JOIN blog_post ON blog_comment.post_id = blog_post.id
ORDER BY blog_comment.data_postagem DESC;"""

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
    texto = row[1][:40] + "..." if len(row[1]) > 40 else row[1]
    print(f"{row[0]} | {texto} | {row[2]} | {row[3]} | {row[4]}")

print(f"\nTotal de registros: {len(results)}\n")

conn.close()
