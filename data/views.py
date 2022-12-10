from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import school, subject, teacher
from .forms import schoolform, subjectform, teacherform

# Create your views here.
class Homeview(TemplateView):
    template_name="index.html"
# Create operations
class newschool(CreateView):
    model = school
    form_class = schoolform
    template_name = 'create.html'

class newsubject(CreateView):
    model = subject
    form_class = subjectform
    template_name = 'create.html'

class newteacher(CreateView):
    model = teacher
    form_class = teacherform
    template_name = 'create.html'

# List operations
class listschool(ListView):
    model = school
    template_name = 'schoollist.html'

class listsubject(ListView):
    model = subject
    template_name = 'subjectlist.html'

class listteacher(ListView):
    model = teacher
    template_name = 'teacherlist.html'