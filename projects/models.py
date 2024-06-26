from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(null=True,blank=True)
    year=models.CharField(max_length=4,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.title


