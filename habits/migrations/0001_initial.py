# Generated by Django 5.0.6 on 2024-06-23 22:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Место"
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Время выполнения"
                    ),
                ),
                ("action", models.CharField(max_length=150, verbose_name="Действие")),
                (
                    "is_nice",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "is_publish",
                    models.BooleanField(
                        default=False, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "time_to_done",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Время для выполнения"
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Вознагрождение",
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        default=1,
                        verbose_name="Периодичность выполнения привычки(кол-во дней)",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]