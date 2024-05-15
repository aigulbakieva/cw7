from rest_framework.generics import CreateAPIView, ListAPIView

from users.models import User
from users.serializer import UserSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
