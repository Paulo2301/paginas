from django.urls import path
from .views import ListagemView, PostagemDetailView,  PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post_delete'),
path('post/<int:pk>/edit/', PostUpdateView.as_view(),name='post_edit'),
path('post/new/', PostCreateView.as_view(), name='post_new'),
path('post/<int:pk>/', PostagemDetailView.as_view(), name='post_detail'),   
path('', ListagemView.as_view(), name ='listagem'),
]