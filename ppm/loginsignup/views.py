from django.shortcuts import render
import email
from django.http.response import HttpResponse
from rest_framework.response import Response
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import MyUser
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group, update_last_login
from rest_framework import status
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.contrib.auth.decorators import login_required

# Create your views here.

class Registration(generics.CreateAPIView):
    serializer_class=RegistrationSerializer
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data = request.data)
            data={}
            if serializer.is_valid():
                my_user = serializer.save()
                token = Token.objects.get(user = my_user).key
                data['old_token']=token
                data['username']=my_user.username
                # data['is_organizer']=my_user.is_organizer
                current_site = 'http://127.0.0.1:8000/'
                relative_link = reverse('verifyEmail')          
                absurl = current_site + relative_link + "?token="+str(token) 
                email_body = 'Hi ' + my_user.username + ' Use link below to verify your email \n' + absurl  
                data_email = {'email_body': email_body, 'to_email': my_user.email, 'email_subject':'Verify your email'}     
                Util.send_email(data_email)           
            else:
                data=serializer.errors
            return Response(data)


@api_view(['GET'])
@permission_classes(())
def verifyEmail(request): 
    data = {}
    token = request.GET.get('token')
    try:
        user = MyUser.objects.get(auth_token = token)
    except:
        content = {'detail': 'User already activated!'}
        return Response(content, status = status.HTTP_200_OK)
    token = request.GET.get('token')
    data['response'] = "successfully registered a new user"
    data['email'] = user.email
    data['user_id']=user.user_id
    data['username']=user.username
    user.is_active = True
    user.save()
    Token.objects.get(user = user).delete()
    Token.objects.create(user = user)
    new_token = Token.objects.get(user = user).key
    data['new_token'] = new_token
    return Response(data)


class LoginView(generics.CreateAPIView):
    serializer_class=loginSerializer
    def post(self,request):
        if request.method == 'POST':
            serializer = loginSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            user = MyUser.objects.get(email = serializer.data['email'])
            token = Token.objects.get(user = user).key
            update_last_login(None, user) #update last login
            data = {}
            data['email'] = user.email
            data['token'] = token
            data['user_id']=user.user_id
            data['username']=user.username
            # data['is_organizer']=user.is_organizer
            return Response(data, status = status.HTTP_200_OK)
# Create your views here.
