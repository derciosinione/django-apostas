from math import trunc
from .models import Partida, Aposta, User, Ranking
from django.shortcuts import get_object_or_404


def contextVencedores(pk):
    
    partida = get_object_or_404(Partida, pk=pk)
    vencedores = partida.apostas.filter(placar1=partida.placar1, placar2=partida.placar2)
    apostadores = partida.apostas.all()
    
    premio = 0
    valorAposta = 5
    totMontant = 0
    totApostas = partida.apostas.count()
    
    if totApostas > 0 :
        totMontant = totApostas * valorAposta
        premio = totMontant
    elif vencedores.count() > 0 :
        premio = trunc((totMontant / vencedores.count()))
        
        
    context = {
        'partida': partida,
        'vencedores': vencedores,
        'apostadores': apostadores,
        'aposta': {
            'totApostas': totApostas,
            'valorAposta' : valorAposta,
            'totMontant': totMontant,
            'premio': premio,  
        }
    }
    return context 