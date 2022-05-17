from django.contrib import admin

from .models import Aadhar, Address, Bank, ContactNumber, Email, JobExp, PersonalDetails, Qualification

# Register your models here.
admin.site.register(Aadhar)
admin.site.register(Address)
admin.site.register(Qualification)
admin.site.register(Bank)
admin.site.register(PersonalDetails)
admin.site.register(ContactNumber)
admin.site.register(Email)
admin.site.register(JobExp)
