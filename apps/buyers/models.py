from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    numberphone = models.CharField('Telefone', max_length=20)

    class Meta:
        verbose_name = 'Comprador'
        verbose_name_plural = 'Compradores'
        ordering =['id']

    def __str__(self):
        return self.name