
from django.urls        import path
from rest_auth.views    import LoginView, LogoutView

from .views             import RegisterUserView



urlpatterns = [
    path('/login/', LoginView.as_view(), name="user-login"),
    path('/logout/', LogoutView.as_view(), name='user-logout'),
    path('/signup/', RegisterUserView.as_view(), name='registration'),
]