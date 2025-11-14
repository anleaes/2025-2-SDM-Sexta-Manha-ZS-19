from django.db import models

# Create your models here.
class Seller(models.Model):
    # Atributos do seu diagrama
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    # Atributo extra para cumprir a regra dos 4 atributos
    phone = models.CharField('Telefone', max_length=20, blank=True)

    # Meta e str baseados no Roteiro-06
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering =['id']

    def __str__(self):
        return self.name
