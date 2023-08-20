from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    joined = models.DateTimeField()
    #image = models.ImageField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.number}'
    class Meta:
        verbose_name='öğrenci'
        verbose_name_plural = 'öğrenciler'
        ordering = ['first_name']
