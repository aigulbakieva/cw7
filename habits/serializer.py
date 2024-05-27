from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedHabitAwardValidator, TimeValidator, IsNiceValidator, RelatedHabitIsNiceValidator, \
    PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedHabitAwardValidator(field1='related_habit', field2='award'),
            TimeValidator(field='time_to_done'),
            RelatedHabitIsNiceValidator(field1='related_habit', field2='is_nice'),
            IsNiceValidator(field1='related_habit', field2='is_nice', field3='award'),
            PeriodValidator(field='period')
        ]
