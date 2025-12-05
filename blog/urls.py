from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('criar/', views.criar_post, name='criar_post'),
    path('<int:id>/', views.detalhe_post, name='detalhe_post'),
    path('<int:id>/editar/', views.editar_post, name='editar_post'),
    path('<int:id>/excluir/', views.excluir_post, name='excluir_post'),
]
