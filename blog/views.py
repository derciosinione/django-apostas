from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.db import IntegrityError
from django.contrib import messages

from .utils import contextVencedores
from .models import Partida, Aposta, User, Ranking


class PartidasListView(LoginRequiredMixin, ListView):
    model = Partida
    template_name = 'blog/partidas.html'
    context_object_name = 'partidas'
    ordering = ['-id']
    paginate_by = 5


class PartidaDetailView(LoginRequiredMixin, DetailView):
    model = Partida
    template_name = 'blog/apostar.html'
    context_object_name = 'partida'


@login_required
def PartidaConcluida(request, pk):
    return render(request, 'blog/partida-detail.html', contextVencedores(pk))
    
    
class PartidaUpdateView(LoginRequiredMixin, UpdateView):
    model = Partida
    template_name = 'blog/atualizarPartida.html'
    context_object_name = 'partida'
    fields = ['placar1','placar2','concluido']
    
    # Verificar se o usuário que está tentar editar o post é o mesmo que criou
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
class ApostasListView(LoginRequiredMixin, ListView):
    model = Aposta
    template_name = 'blog/apostas.html'
    context_object_name = 'apostas'
    ordering = ['-id']
    paginate_by = 5
    
    # Sobrescrever a queryset padrão da ListView
    def get_queryset(self):
        return Aposta.objects.filter(user=self.request.user).order_by('-id')


class JogadoresListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'blog/jogadores.html'
    context_object_name = 'jogadores'
    ordering = ['-credito__valor']
    paginate_by = 5


def Apostar(request, idpartida):
    """[Efectuar Apostas]
    Este metodo serve para criar uma nova aposta,
    primeiramente é selecionada a partida e o usuario que está efectuando a ação,
    depois é verificado se o jogador tem saldo suficiente na conta para efectuar a aposta.    
    """
    try:

        if request.method=='POST':
            
            partida = get_object_or_404(Partida, pk=idpartida)
            user = request.user
            valor_fixo = 5
            
            # Verificar se o jogador tem saldo suficiente para apostar
            if user.credito.valor >= valor_fixo:
                # Efectuar o desconto do credito do jogador para concluir a aposta
                user.credito.valor -= valor_fixo
                
                # Criar a instancia da aposta para salvar os dados na BD.
                aposta = Aposta(user=user, partida=partida, placar1=request.POST['placar1'], placar2=request.POST['placar2']) 
                aposta.save() # salvar a aposta.
                user.save()
                
                # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
                messages.success(request,f'Aposta da partida {partida.equipe1} vs {partida.equipe2} efectuada com sucesso!')
            else:
                # Criar mensagem de erro, porque o usuario não tem valor suficiente para apostar.
                messages.error(request,'ups!!! O seu saldo é insuficiente para efectuar esta operação, recarregue o seu cartão para continuar apostar.')

                # Redirecionar o usuario para rota de partidas.
                return redirect('blog:partidas') 
            
    except IntegrityError: # O sistema cairá nesta excessão de erro caso tentar apostar mais de uma vez numa partida. 
        messages.error(request,'Não é possivel efectuar múltiplas apostas em uma partida, por favor selecione outra partida.')
        return redirect('blog:partidas')

    return redirect('blog:apostas')


def EntregarPremio(request, pk):
    
    data = contextVencedores(pk)
    vencedores = data['vencedores']
    apostadores = data['apostadores']
    premio = data["aposta"]["premio"]

    if len(vencedores) > 0 :
        for aposta in data['vencedores']:
            user = aposta.user
            user.credito.valor += premio
            Ranking.objects.create(user=user, aposta=aposta, premio=premio)
            user.save()        
        # Criar mensagem de sucesso, pois a operação foi efectuada com sucesso.
        mensagem = f'Premio distribuido para {len(vencedores)} jogador(es) com sucesso...'

    elif apostadores:
        for aposta in apostadores :
            user = aposta.user
            user.credito.valor += 5
            user.save()

        mensagem = f'Valor de aposta devolvido para {len(apostadores)} jogador(es) com sucesso...'
    
    #Encerrar a premiação das partidas
    partida = data['partida']
    partida.encerrado = True
    partida.save()
    
    messages.success(request,mensagem)
    
    return redirect('blog:jogadores')

