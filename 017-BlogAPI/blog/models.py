from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(verbose_name='Kategori Adı', max_length=64)

    class Meta:
        verbose_name= 'Blog kategori'
        verbose_name_plural= 'Blog kategorileri'


    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='Kullanıcı', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Kategori', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Başlık', max_length=128)
    content = models.TextField(verbose_name='İçerik')
    created_date = models.DateTimeField(verbose_name='Oluşturulma T.', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Güncelleme T.',auto_now=True)

    class Meta:
        verbose_name= 'Blog yazısı'
        verbose_name_plural= 'Blog yazıları'

    def __str__(self):
        return f'{self.category} /{self.title}'