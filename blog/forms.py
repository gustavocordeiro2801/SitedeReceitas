from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'ingredientes', 'modo_preparo']
        widgets = {
            'titulo': forms.TextInput(attrs={'size': '60'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 60, 'placeholder': 'Uma breve descrição da receita...'}),
            'ingredientes': forms.Textarea(attrs={'rows': 8, 'cols': 60, 'placeholder': 'Ex: xícaras de farinha, 1 xícara de açúcar'}),
            'modo_preparo': forms.Textarea(attrs={'rows': 10, 'cols': 60, 'placeholder': 'Ex: Misture os ingredientes secos, Adicione os líquidos'}),
        }
        labels = {
            'titulo': 'Título da Receita',
            'descricao': 'Descrição (opcional)',
            'ingredientes': 'Ingredientes (pode usar HTML)',
            'modo_preparo': 'Modo de Preparo (pode usar HTML)',
        }
