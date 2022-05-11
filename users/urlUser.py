# from users.viewsets import UserViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'users', UserViewSet, basename='user')


from django.urls import path
from users.views import Register, Login, Logout
urlpatterns = [
    path('register',  Register.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view())
]