from .models import school, subject, teacher
from django import forms

class schoolform(forms.ModelForm):
    class Meta:
        model = school
        fields = '__all__'

class subjectform(forms.ModelForm):
    class Meta:
        model = subject
        fields = '__all__'

class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = '__all__'
