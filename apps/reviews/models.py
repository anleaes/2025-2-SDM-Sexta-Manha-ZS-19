from django.db import models
from buyers.models import Buyer
from sellers.models import Seller

# Modelo de Avaliações entre Compradores e Vendedores

class Review(models.Model):
    # Foreign Keys
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name='Comprador')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Vendedor Avaliado')
    

    rating = models.IntegerField('Nota', choices=[(i, i) for i in range(1, 6)]) # 1 a 5 estrelas
    comment = models.TextField('Comentário', max_length=500)
    date = models.DateField('Data da Avaliação', auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # Ordenei da mais recente para a mais antiga
        ordering =['-date']

    def __str__(self):
        return f"Avaliação de {self.buyer.name} para {self.seller.name}"
