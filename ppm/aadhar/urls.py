from django.urls import path
from .views import *

urlpatterns = [
    path('',AadharAPI.as_view(), name='Aadhar Details'),
    path('address/',AddressAPI.as_view(), name='All Address'),
    path('address/<int:pk>/', UpdateDestroyAddressView.as_view(), name='Address Update & Delete'),
    path('qualification/',QualificationAPI.as_view(), name='Aadhar Details'),
    path('qualification/<int:pk>/',UpdateDestroyQualificationView.as_view(),name='All Qualification'),
    path('bank/',BankAPI.as_view(), name='Aadhar Details'),
    path('bank/<int:pk>/',UpdateDestroyBankView.as_view(),name='Qaulification Details'),
    path('perdet/',PerDetAPI.as_view(), name='Aadhar Details'),
    path('perdet/<int:pk>/',UpdateDestroyPerDetAPIView.as_view(),name='Qaulification Details'),
]