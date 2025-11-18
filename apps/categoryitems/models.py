from django.db import models
from categories.models import Category 
from items.models import Item 


class CategoryItem(models.Model):
    # Foreign Keys (Chaves Estrangeiras)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    is_primary = models.BooleanField('Categoria Principal', default=False)
    created_at = models.DateField('Data de Ligação', auto_now_add=True)

    class Meta:
        # Garante que um item só possa ser ligado uma vez à mesma categoria
        unique_together = ('category', 'item')
        verbose_name = 'Item da Categoria'
        verbose_name_plural = 'Itens da Categoria'
        ordering =['id']

    def __str__(self):
        return f"{self.item.title} - {self.category.name}"
