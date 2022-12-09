from django.urls import path
from . import views

#app_name = "scanner"   


urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path('', views.register_request, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.login, name='profile'),
    path('error', views.login, name='error')
]