from django.db import models
from django.urls import reverse

# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")

class subject(models.Model):
    name = models.CharField(max_length=200,unique=True)
    tutor = models.CharField(max_length=200)
    std_no = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("index")

class teacher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE, blank=True)
    school = models.ForeignKey(school, on_delete=models.CASCADE, blank = True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("index")
