from django.db import models
from django.conf import settings
from django.urls import reverse


class Clients(models.Model):
    class Status(models.TextChoices):
        in_progress = "in_progress", "В работе"
        not_in_work = "not_in_work", "Не в работе"
        refusal = "refusal", "Отказ"
        deal_closed = "deal_closed", "Сделка закрыта"

    account_number = models.IntegerField(unique=True, db_index=True, verbose_name="Номер счета")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    date_birth = models.DateField(verbose_name="Дата рождения")
    inn = models.IntegerField(unique=True, db_index=True, verbose_name="ИНН")
    status = models.CharField(max_length=255, choices=Status, default=Status.not_in_work,
                              verbose_name="Статус")

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                default=settings.AUTH_USER_MODEL, verbose_name="Ответственное лицо")

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return 'http://127.0.0.1:8000/main/'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
