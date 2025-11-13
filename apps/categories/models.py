from django.db import models
# Classe para categorizar os itens do leilão
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    is_active = models.BooleanField('Ativo', default=True)
    registration_date = models.DateField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name


