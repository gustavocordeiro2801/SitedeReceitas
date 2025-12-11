import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Pegar o post que tem MAIS comentários
cursor.execute("""
    SELECT post_id, COUNT(*) as total 
    FROM blog_comment 
    GROUP BY post_id 
    ORDER BY total DESC 
    LIMIT 1
""")
post_com_comentario = cursor.fetchone()

if post_com_comentario:
    post_id = post_com_comentario[0]
    total_comentarios = post_com_comentario[1]
    
    # Pegar o título do post
    cursor.execute(f"SELECT titulo FROM blog_post WHERE id = {post_id}")
    titulo = cursor.fetchone()[0]
    
    print("\n" + "=" * 100)
    print(f"QUERY 2: Listar todos os comentários do post ID {post_id}")
    print(f"Post: '{titulo}' ({total_comentarios} comentários)")
    print("=" * 100)
    
    query = f"""SELECT * FROM blog_comment
WHERE post_id = {post_id}
ORDER BY data_postagem DESC;"""
    
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
        texto = row[1] if len(row[1]) <= 50 else row[1][:50] + "..."
        print(f"{row[0]} | {texto} | {row[2]} | {row[3]} | {row[4]}")
    
    print(f"\nTotal de registros: {len(results)}\n")
else:
    print("\nNenhum comentário encontrado no banco de dados.\n")

conn.close()
