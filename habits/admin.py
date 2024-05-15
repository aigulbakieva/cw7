from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'owner', 'place', 'time', 'action', 'is_nice', 'related_habit', 'is_publish', 'time_to_done', 'award',)
