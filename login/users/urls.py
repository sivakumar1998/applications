from django.urls import path
from . import views
app_name='users'

urlpatterns=[
    path("",views.register,name='register'),
    path('welcome/',views.welcome,name='welcome')
]