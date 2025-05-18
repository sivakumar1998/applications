from django.urls import path
from django.contrib.auth import views as auth_views
app_name='login'
urlpatterns=[
   path('login/',auth_views.LoginView.as_view(template_name='signin/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='signin/logout.html'),name='logout')
]