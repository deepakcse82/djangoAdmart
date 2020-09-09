from django.urls import path
from adweb import views as web


urlpatterns = [
    path('', web.web_home, name='home'),
    path('login/', web.login, name='login'),
    path('register/', web.register, name='register'),
]