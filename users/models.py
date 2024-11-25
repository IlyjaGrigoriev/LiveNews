from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS_CHOICES = [
        ('author', 'Автор статей'),
        ('reader', 'Читатель')
    ]
    phone_number = models.CharField(
        'Номер телефона',
        max_length=12
        
    )
    father_name = models.CharField(
        'Отчество',
        max_length=50,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Ваша фотография',
        upload_to='users/',
        blank=True
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='customer',
        verbose_name="Статус пользователя",
        max_length=50,
    )

    # class Meta:
    #     verbose_name = 'Пользователь'
    #     verbose_name_plural = 'Пользователи'
