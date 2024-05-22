from datetime import timezone

from celery import shared_task
from django.utils import timezone
from datetime import datetime

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habits_information():
    today = timezone.now()
    time_now = today.strftime("%m/%d/%Y, %H:%M")
    habits_to_send = Habit.objects.filter(is_nice=False)
    for habit in habits_to_send:
        task_time = datetime.strftime(habit.time, "%m/%d/%Y, %H:%M")
        if task_time == time_now:
            tg_id = habit.owner.telegram_id
            message = f"Выполните привычку: {habit.action}  время:{habit.time} место: {habit.place}"
            send_telegram_message(tg_id, message)
        habit.save()
