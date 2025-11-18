from django.db import models
from buyers.models import Buyer
from auctions.models import Auction
# Modelo para o registro de Lances

class Bid(models.Model):
    
    amount = models.DecimalField('Valor do Lance', max_digits=10, decimal_places=2)
    time = models.TimeField('Hora do Lance', auto_now_add=True)
    date = models.DateField('Data do Lance', auto_now_add=True)
    
    # Relações (Foreign Keys)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name='Comprador')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, verbose_name='Leilão')
    
    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lances'
        # Garante que um comprador não dê lances duplicados exatos
        unique_together = ('buyer', 'auction', 'amount') 
        # Ordenado do mais novo para o mais antigo (data e hora)
        ordering =['-date', '-time']

    def __str__(self):
        return f"Lance de {self.amount} por {self.buyer.name} no Leilão {self.auction.title}"