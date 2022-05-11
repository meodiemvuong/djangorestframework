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
        if 'email' not in data or 'password' not in data:
            raise exceptions.APIException({
                "message": "Please enter email or password"
            })
        try:
            user = User.objects.get(email=data.get('email'))
        except User.DoesNotExist:
            raise exceptions.APIException({
                "message": "User not Found"
            })
        if not user.check_password(data.get('password')):
            raise exceptions.APIException({
                "message": "Password incorrect"
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

#Logout
class Logout(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def post(self, req):
        logout(req)
        return Response({
            "message": "Logout success"
        })

#Current User Detai
class CurrentUser(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def get(self, req):
        user = User.objects.get(id=req.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Change Password
class ChangePassword(APIView):
    permission_classes = [(permissions.IsAuthenticated)]
    def post(self, req):
        data = req.data
        if 'oldpassword' not in data or 'newpassword' not in data:
            raise exceptions.APIException({
                "message": "Please enter oldpassword or new password"
            })
        #Check oldpassword
        user = User.objects.get(id=req.user.id)
        if not user.check_password(data.get('oldpassword')):
            raise exceptions.APIException({
                "message": "Password incorrect"
            })
        
        if not len(data.get('newpassword'))>=6:
            raise exceptions.APIException({
                "message": "Newpassword is more than 6 character"
            })
        user.set_password(data.get('newpassword'))
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        # serializer.data
