from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fio = models.CharField('ФИО', max_length=255, default='')
    # Обязательно удалить старую бд, и все миграции
    # И сначала сделать (makemigrations users), иначе потом посыпятся ошибки