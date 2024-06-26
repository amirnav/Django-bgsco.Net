from django.db import models

class hiring(models.Model):
    class marrySit(models.TextChoices):
        SINGLE="SN", "Single"
        MARRIED="MR","Married"

    firstName=models.CharField(max_length=20,verbose_name="First Name")
    lastName=models.CharField(max_length=20,verbose_name="Last Name",null=True,blank=True)
    fatherName=models.CharField(max_length=20,verbose_name="Father Name",null=True,blank=True)
    NationalId=models.CharField(max_length=10,verbose_name="National Id",blank=True,null=True)
    marriageSituate=models.CharField(max_length=50,choices=marrySit,verbose_name="Married Situate",null=True,blank=True)
    country=models.CharField(max_length=50,verbose_name="Country",null=True,blank=True)
    address=models.CharField(max_length=200,verbose_name="Address",null=True,blank=True)
    birthdayDate=models.DateField(verbose_name="Date of Birthday",null=True,blank=True)
    phone=models.CharField(max_length=11,verbose_name="Mobile Phone",null=True,blank=True)
    email=models.EmailField(verbose_name="Email",blank=True,null=True)
    fileUpload = models.FileField(upload_to='documents/%Y/%m/%d')
    city=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.firstName