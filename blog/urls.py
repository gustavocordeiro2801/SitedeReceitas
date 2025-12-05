from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaPostsView.as_view(), name='lista_posts'),
    path('criar/', views.CriarPostView.as_view(), name='criar_post'),
    path('<int:id>/', views.DetalhePostView.as_view(), name='detalhe_post'),
    path('<int:id>/editar/', views.EditarPostView.as_view(), name='editar_post'),
    path('<int:id>/excluir/', views.ExcluirPostView.as_view(), name='excluir_post'),
]
