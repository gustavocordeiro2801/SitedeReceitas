from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)  # Descrição breve da receita
    ingredientes = models.TextField()  # Lista de ingredientes (HTML)
    modo_preparo = models.TextField()  # Modo de preparo (HTML)
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
