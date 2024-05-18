from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateApiView, HabitListApiView, HabitRetrieveApiView, HabitDestroyApiView, \
    HabitUpdateApiView, PublishHabitListApiView

app_name = HabitsConfig.name


urlpatterns = [
    path("", HabitListApiView.as_view(), name='habit-list'),
    path("<int:pk>/", HabitRetrieveApiView.as_view(), name='habit-retrieve'),
    path("create/", HabitCreateApiView.as_view(), name='habit-create'),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name='habit-delete'),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name='habit-update'),
    path("published/", PublishHabitListApiView.as_view(), name='habit-publish'),
]
