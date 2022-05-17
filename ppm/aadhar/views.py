from django.shortcuts import render
from .serializers import *
from rest_framework import (mixins, generics, status, permissions)
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponse, JsonResponse
# Create your views here.
class AadharAPI(generics.ListCreateAPIView):
    serializer_class = AadharSerializer
    queryset = Aadhar.objects.all()
    permission_classes = [IsAuthenticated]


class AddressAPI(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateDestroyAddressView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Address.objects.all()
    serializer_class= AddressSerializer
    permission_classes = [IsAuthenticated]

class QualificationAPI(generics.ListCreateAPIView):
    serializer_class = QualificationSerializer
    queryset = Qualification.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateDestroyQualificationView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Qualification.objects.all()
    serializer_class= QualificationSerializer
    permission_classes = [IsAuthenticated]

class BankAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateDestroyBankView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Bank.objects.all()
    serializer_class= BankSerializer
    permission_classes = [IsAuthenticated]

class PerDetAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = PersonalDetailsSerializer
    queryset = PersonalDetails.objects.all()
    permission_classes = [IsAuthenticated]

class UpdateDestroyPerDetAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= PersonalDetails.objects.all()
    serializer_class= PersonalDetailsSerializer
    permission_classes = [IsAuthenticated]
