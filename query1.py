import sqlite3
import os

# Conectar ao banco de dados
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n" + "=" * 100)
print("QUERY 1: Listar todos os posts ordenados por data de postagem (mais recentes primeiro)")
print("=" * 100)

query = """SELECT * FROM blog_post
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
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3][:50] if row[3] else 'NULL'}... | ...")

print(f"\nTotal de registros: {len(results)}\n")

conn.close()
