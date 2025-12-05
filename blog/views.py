from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# LISTAGEM
def lista_posts(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'blog/lista.html', {'posts': posts})

# DETALHE
def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detalhe.html', {'post': post})

# CRIAR POST (sem forms)
def criar_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        ingredientes = request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')

        Post.objects.create(
            titulo=titulo,
            descricao=descricao,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo
        )

        return redirect('lista_posts')

    return render(request, 'blog/criar.html')

# EDITAR POST (sem forms)
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.descricao = request.POST.get('descricao')
        post.ingredientes = request.POST.get('ingredientes')
        post.modo_preparo = request.POST.get('modo_preparo')
        post.save()
        return redirect('detalhe_post', id=post.id)

    return render(request, 'blog/editar.html', {'post': post})

# EXCLUIR POST (com confirmação)
def excluir_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'blog/excluir_confirmar.html', {'post': post})
