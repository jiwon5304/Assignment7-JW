from rest_framework             import generics
from rest_framework.generics    import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth        import get_user_model

from .models                    import User
from .serializers               import RegisterUserSerializer


class RegisterUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class   = RegisterUserSerializer