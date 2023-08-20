from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default='none@cw.com', null=True, blank=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', default='',null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # created = models.DateTimeField(default='timezone.now', auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True, )
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.number}'
    class Meta:
        verbose_name='öğrenci'
        verbose_name_plural = 'öğrenciler'
        ordering = ['first_name']


# --------------------django shell

AGES = [
    (0,'yaş: 0'),
    (10,'yaş: 10'),
    (20,'yaş: 20'),
    (30,'yaş: 30'),
    (40,'yaş: 40'),
]


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, blank=True, null=True, choices=AGES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}-{self.age}'
    
    class Meta:
        verbose_name='Müşteri'
        verbose_name_plural = 'Müşteriler'
        ordering = ['-age']