# from users.viewsets import UserViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'users', UserViewSet, basename='user')


from django.urls import path
from users.views import Register, Login, Logout, CurrentUser, ChangePassword
urlpatterns = [
    path('register',  Register.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),
    path('me', CurrentUser.as_view()),
    path('changepassword', ChangePassword.as_view())
]