from django.db import models

# Create your models here.
class Item(models.Model):
    # Atributos do seu diagrama + is_active para fechar 4 atributos
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição')
    min_bid = models.DecimalField('Lance Mínimo', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering =['id']

    def __str__(self):
        return self.title
