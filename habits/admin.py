from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'place', 'time', 'action', 'is_nice', 'related_habit', 'time_to_complete', 'is_publish',)
