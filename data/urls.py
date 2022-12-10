from django.urls import path, include
from data.views import Homeview, newschool, newsubject, newteacher, listschool, listteacher, listsubject

urlpatterns = [
    path('', Homeview.as_view(), name="index"),
    path('create-school', newschool.as_view(), name="newschool"),
    path('create-subject', newsubject.as_view(), name="newsubject"),
    path('create-teacher', newteacher.as_view(), name="newteacher"),
    path('list-school', listschool.as_view(), name="listschool"),
    path('list-subject', listsubject.as_view(), name="listsubject"),
    path('list-teacher', listteacher.as_view(), name="listteacher"),
]
