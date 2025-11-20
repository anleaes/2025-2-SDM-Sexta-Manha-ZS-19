from django.db import models
from buyers.models import Buyer
from auctions.models import Auction

# Modelo para o registro de Pagamentos

class Payment(models.Model):

    TYPE_CHOICES = [
        ('pix', 'PIX'),
        ('credit_card', 'Cartão de Crédito'),
        ('bank_transfer', 'Transferência Bancária'),
    ]
    
    
    amount = models.DecimalField('Valor Pago', max_digits=10, decimal_places=2)
    type = models.CharField('Tipo de Pagamento', max_length=20, choices=TYPE_CHOICES)
    date = models.DateField('Data do Pagamento', auto_now_add=True)
    
    # Relações (Foreign Keys)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name='Comprador')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, verbose_name='Leilão Pago')
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['-date']

    def __str__(self):
        return f"Pagamento de {self.amount} ({self.type})"