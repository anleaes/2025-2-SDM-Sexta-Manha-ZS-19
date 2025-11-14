from django.db import models

# Modelo para os Vendedores

class Seller(models.Model):

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)


    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering =['id']

    def __str__(self):
        return self.name
