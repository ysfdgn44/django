from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField( max_length=256)

    def __str__(self):
        return f'{self.username}'
    

class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    about = models.TextField()
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account} - {self.first_name} {self.last_name}'
    
COUNTRIES = [
    ('US', 'America'),
    ('DE', 'Germany'),
    ('TR', 'Turkey'),
]

class Address(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField()
    country = models.CharField(max_length=2, choices=COUNTRIES)
    phone = models.CharField(max_length=16)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account} - {self.name} {self.country}'
    
class Product(models.Model):
    brand = models.CharField(verbose_name='Marka', max_length=64)
    product = models.CharField('Ürün Adı', max_length=64)
    account = models.ManyToManyField(Account, verbose_name='Hesaplar')

    def __str__(self):
        return f'{self.brand} {self.product}'
    
    class Meta:
        verbose_name = 'ürün'
        verbose_name_plural = 'ürünler'

