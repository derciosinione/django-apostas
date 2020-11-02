from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Credito


@receiver(post_save,sender=User)
def create_credito(sender, instance, created, **kwargs):
    if created:
        Credito.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_credito(sender, instance, **kwargs):
    instance.credito.save()
    
    
# @receiver(post_save,sender=User)
# def create_perfil(sender, instance, created, **kwargs):
#     if created:
#         Credito.objects.create(user=instance)
        
# @receiver(post_save,sender=User)
# def save_perfil(sender, instance, **kwargs):
#     instance.perfil.save()