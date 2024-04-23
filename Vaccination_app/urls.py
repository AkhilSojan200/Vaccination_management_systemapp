from django.urls import path
from Vaccination_app import views


urlpatterns = [

path('',views.index, name='index'),

]