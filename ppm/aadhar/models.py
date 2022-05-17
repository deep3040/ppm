from django.db import models
# Create your models here.
class Aadhar(models.Model):
    aadhar_no = models.CharField(primary_key=True, max_length=12)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.aadhar_no

class Address(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE, null=True, blank=True)
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    post_code = models.CharField(max_length=6)

    def __str__(self):
        return str(self.aadhar)

class Qualification(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
    yearofpassing = models.PositiveIntegerField()
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return str(self.aadhar)

class Bank(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE, null=True, blank=True)
    acc_no = models.CharField(max_length=20)
    bank_name = models.TextField()
    ifsc = models.CharField(max_length=11)

    def __str__(self):
        return str(self.aadhar)

class PersonalDetails(models.Model):
    aadhar = models.OneToOneField(Aadhar,on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    blood_grp = models.CharField(max_length=3)

    def __str__(self):
        return str(self.aadhar)

class ContactNumber(models.Model):
    per = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    number = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.per)

class Email(models.Model):
    per = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return str(self.per)

class JobExp(models.Model):
    aadhar = models.ForeignKey(Aadhar,on_delete=models.CASCADE, null=True, blank=True)
    comp_name = models.TextField()
    role = models.TextField()
    work_exp = models.PositiveIntegerField()

    def __str__(self):
        return str(self.aadhar)
