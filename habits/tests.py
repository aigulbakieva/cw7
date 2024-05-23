from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.pro",
            password="123qwe",
            is_active=True,
            is_staff=True,
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            action="Читать книгу",
            place="дом",
            is_nice=False,
        )
