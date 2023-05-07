from django.urls import path
from fitforge import views

app_name = 'fitforge'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
