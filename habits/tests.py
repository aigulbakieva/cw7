from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.pro",
            password="123qwe",
            is_active=True,
            is_staff=True
        )
        self.user.set_password("123qwe")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            action="Читать книгу",
            place="дом",
            is_nice=True
        )

    def test_habit_create(self):
        url = reverse("habits:habit-create")
        data = {
            "owner": self.user.pk,
            "action": "test",
            "place": "test",
            "is_nice": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_habit_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "test",
                    "action": "test",
                    "owner": self.user.pk,
                }, ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_update(self):
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {
            "place": "test",
            "action": "test",
            "owner": self.user.pk,
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_habit_delete(self):
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        data = {
            "place": "test",
            "action": "test",
            "owner": self.user.pk,
        }
        response = self.client.delete(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0)

    def test_habit_time_to_done(self):
        url = reverse("habits:habit-create")
        data = {
            "place": "test",
            "action": "test",
            "owner": self.user.pk,
            "time_to_done": "130"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_habit_rel_hab_award(self):
        url = reverse("habits:habit-create")
        data = {
            "place": "test",
            "action": "test",
            "owner": self.user.pk,
            "related_habit": "2",
            "award": "test"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
