from django.contrib import admin
from .models import school, subject, teacher

# Register your models here.
admin.site.register(school)
admin.site.register(subject)
admin.site.register(teacher)