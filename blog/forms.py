from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'ingredientes', 'modo_preparo']
        widgets = {
            'titulo': forms.TextInput(attrs={'size': '60'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'cols': 60, 'placeholder': 'Uma breve descrição da receita...'}),
            'ingredientes': forms.Textarea(attrs={'rows': 8, 'cols': 60, 'placeholder': 'Ex: <ul><li>2 xícaras de farinha</li><li>1 xícara de açúcar</li></ul>'}),
            'modo_preparo': forms.Textarea(attrs={'rows': 10, 'cols': 60, 'placeholder': 'Ex: <ol><li>Misture os ingredientes secos</li><li>Adicione os líquidos</li></ol>'}),
        }
        labels = {
            'titulo': 'Título da Receita',
            'descricao': 'Descrição (opcional)',
            'ingredientes': 'Ingredientes (pode usar HTML)',
            'modo_preparo': 'Modo de Preparo (pode usar HTML)',
        }
