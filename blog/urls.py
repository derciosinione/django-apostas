from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import ( 
                    Apostar, 
                    ApostasListView, 
                    JogadoresListView, 
                    PartidasListView,
                    PartidaDetailView, 
                    PartidaUpdateView,
                    EntregarPremio,
                    PartidaConcluida 
                    ) 


app_name = 'blog'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('sair/', auth_views.LogoutView.as_view(),name='sair'),
    path('partidas/', PartidasListView.as_view(), name='partidas'),
    path('partida/<int:pk>/', PartidaDetailView.as_view(), name='partida'),
    path('partida/<int:pk>/vencedores', PartidaConcluida, name='vencedores'),
    path('partida/<int:pk>/premiar', EntregarPremio, name='premiar-vencedores'),
    path('apostas/', ApostasListView.as_view(), name='apostas'),
    path('jogadores/', JogadoresListView.as_view(), name='jogadores'),
    path('apostar/<int:idpartida>/', Apostar, name='apostar'),
    path('partida/<int:pk>/update', PartidaUpdateView.as_view(), name='partida-update'),
]

