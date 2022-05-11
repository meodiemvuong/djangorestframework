from dataclasses import field
from rest_framework import serializers
from django.core.mail import send_mail
from users.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'email', 'password', 'name', 'gender', 'phone']

    #SendEmail When Create User Success
    def create(self, validated_data):
        password = validated_data.pop('password')
        data = self.Meta.model(**validated_data)
        if len(password) > 6 and password:
            data.set_password(password)
            if data.save():   
                send = send_mail("Create user Success", "Hello " + validated_data['name'], 'thanhbinh16092k1@gmail.com' , [validated_data['email']])
        return data