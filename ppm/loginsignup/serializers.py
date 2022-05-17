from rest_framework import serializers
from .models import *
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login
from rest_framework import (mixins, generics, status, permissions)
from rest_framework.response import Response

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyUser
        fields = ['username','email']
        

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MyUser
        fields = ['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser(
            email             = validated_data['email'],
            username          = validated_data['username'],
            # is_organizer      = validated_data['is_org]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class loginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = MyUser
        fields = ['email', 'password']
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {'email': user.email}

# class LogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'message':'Logged out successfully'},status=status.HTTP_204_NO_CONTENT)