from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def men_get_absolute_url(self):
        return reverse('men_product_list_by_category', args=[self.slug])

    def women_get_absolute_url(self):
        return reverse('women_product_list_by_category', args=[self.slug])

    def boys_get_absolute_url(self):
        return reverse('boys_product_list_by_category', args=[self.slug])

    def girls_get_absolute_url(self):
        return reverse('girls_product_list_by_category', args=[self.slug])



GENDER_CHOICES = (
    ('man', 'man'),
    ('woman', 'woman'),
    ('boys', 'boys'),
    ('girls', 'girls')
)


class Product(models.Model):
    """Модель описания продукта"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию'
                                 )
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наменование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


