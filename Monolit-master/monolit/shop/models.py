from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser (AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Логин', unique=True, blank=False)
    password = models.CharField(max_length=100, verbose_name="Пароль", blank=False)
    email = models.EmailField(max_length=100, verbose_name='Почта', unique=True, blank=False)
    avatar = models.ImageField(verbose_name="Загрузите аватарку", upload_to='avatars')

class Product (models.Model):
    title = models.CharField(max_length=200, blank=False)
    img = models.ImageField(upload_to='image', null=True, blank=True, default=None)
    description = models.TextField(help_text="Введите описание товара")
    date = models.DateTimeField(verbose_name='Дата добавления', null=True, auto_now_add=True)