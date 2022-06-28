from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Credito(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    valor = models.DecimalField(default=100,max_digits=11,decimal_places=2)
    
    def __str__(self):
        return f'{self.user.username} - valor: {self.valor} AO'
    
    
class Equipe(models.Model):
    nome = models.CharField(max_length=50,unique=True,null=False,blank=False)
    
    def __str__(self):
        return f'{self.nome}'
    
    
class Partida(models.Model):
    equipe1 = models.ForeignKey(Equipe,related_name='equipe1',on_delete=models.CASCADE,verbose_name='1ª Equipe')
    equipe2 = models.ForeignKey(Equipe,related_name='equipe2',on_delete=models.CASCADE,verbose_name='2ª Equipe')
    placar1 = models.IntegerField(verbose_name='Placar 1',default=0,help_text='Indica o total de golos da 1ª equipe')
    placar2 = models.IntegerField(verbose_name='Placar 2',default=0,help_text='Indica o total de golos da 2ª equipe')
    data_criada = models.DateTimeField(auto_now_add=True,verbose_name='Data de criação')
    data_partida = models.DateTimeField(default=None,verbose_name='Data da partida')
    concluido = models.BooleanField(default=False)
    encerrado = models.BooleanField(default=False,help_text='Indica se os jogadores ja receberam os prêmios')
    
    
    def __str__(self):
        return f'{self.equipe1.nome} vs {self.equipe2.nome}'
    
    def get_absolute_url(self):
        return reverse('blog:vencedores', kwargs={'pk': self.pk})
    
        
class Aposta(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='apostas')
    partida = models.ForeignKey(Partida,on_delete=models.CASCADE,related_name='apostas')
    placar1 = models.IntegerField(verbose_name='Placar 1',default=0,help_text='Indica o total de golos da 1ª equipe')
    placar2 = models.IntegerField(verbose_name='Placar 2',default=0,help_text='Indica o total de golos da 2ª equipe')
    valor = models.DecimalField(default=5,max_digits=11,decimal_places=2)
    
    def __str__(self):
        return f'{self.user.username} - {self.partida.equipe1} vs {self.partida.equipe2} '
    
    class Meta:
        unique_together = (('user','partida'))


class Ranking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vitorias')
    aposta = models.ForeignKey(Aposta,on_delete=models.CASCADE,related_name='ranking')
    premio = models.DecimalField(default=5,max_digits=11,decimal_places=2)
    data_criada = models.DateTimeField(auto_now_add=True,verbose_name='Data de criação')

    def __str__(self):
        return f'{self.user.username}, Victória: {self.aposta.partida.equipe1} vs {self.aposta.partida.equipe2}'
