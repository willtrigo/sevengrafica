from django.db import models
from django.conf import settings
from django.utils import timezone
from random import shuffle

class CaseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))

class Case(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    image = models.ImageField(upload_to='cases', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    object = CaseManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('cases:products', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
        ordering = ['name']

class ProductManager(models.Manager):
    def random(self, number):
        products = list(self.all()[:number])
        shuffle(products)
        return products

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    image = models.ImageField(upload_to='cases', verbose_name='Imagem', null=True, blank=True)

    case = models.ForeignKey(Case, verbose_name='Case', related_name='products')

    objects = ProductManager()

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
