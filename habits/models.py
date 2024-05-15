from django.db import models
from config import settings


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name="Пользователь")
    place = models.CharField(max_length=50, null=True, blank=True, verbose_name="Место")
    time = models.DateTimeField(verbose_name="Время выполнения", null=True, blank=True)
    action = models.CharField(max_length=150, verbose_name="Действие")
    is_nice = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name="Связанная привычка")
    time_to_complete = models.TimeField(verbose_name="Время для выполнения", null=True, blank=True)
    is_publish = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
