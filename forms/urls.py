from django.urls import path
from .views import about_form, about_list

urlpatterns = [
    path('', about_form, name='about_form'),
    path('list/', about_list, name='about_list')
]