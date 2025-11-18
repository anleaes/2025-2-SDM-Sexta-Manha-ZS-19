from django.db import models
from sellers.models import Seller
from items.models import Item

# Modelo Central de Leilões

class Auction(models.Model):
    
    STATUS_CHOICES = [
        ('draft', 'Rascunho'),
        ('open', 'Aberto'),
        ('closed', 'Fechado'),
        ('finalized', 'Finalizado'),
    ]
    
    
    title = models.CharField('Título do Leilão', max_length=255)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='draft')
    
    # Relações (Foreign Keys)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Vendedor')
    # OneToOneField: Um leilão é para exatamente um item (conforme diagrama)
    item = models.OneToOneField(Item, on_delete=models.CASCADE, verbose_name='Item Leiloado') 
    
    
    class Meta:
        verbose_name = 'Leilão'
        verbose_name_plural = 'Leilões'
        ordering =['-id']

    def __str__(self):
        return f"{self.title} - Status: {self.status}"