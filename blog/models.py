from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)  # Descrição breve da receita
    ingredientes = models.TextField()  # Lista de ingredientes (HTML)
    modo_preparo = models.TextField()  # Modo de preparo (HTML)
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_postagem']  # Mais recentes primeiro

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.post.titulo}"
