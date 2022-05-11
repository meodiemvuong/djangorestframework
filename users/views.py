from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions, exceptions
from django.contrib.auth import login, logout
from users.models import User 
from users.serializers import UserSerializer
# Create your views here.


# Register User
class Register(APIView):
    def post(self, req):
        data = req.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'User': serializer.data,
            'Token': token.key
        })

#Login User
class Login(APIView):
    def post(self, req):
        data = req.data
        print(data)
        if 'email' not in data:
            raise exceptions.APIException({
                "message": "Please enter email and password"
            })
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise exceptions.APIException({
                "message": "User not Found"
            })
        token, created = Token.objects.get_or_create(user=user)
        login(req, user=user)
        response = Response()
        response.set_cookie('token', token)
        response.data = {
            'message': "Login success",
            'token': token.key
        }
        return response

class Logout(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def post(self, req):
        logout(req)

        return Response({
            "message": "Logout success"
        })