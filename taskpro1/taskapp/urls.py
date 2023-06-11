
from django.urls import path
from . import views
app_name = 'taskapp'

urlpatterns = [

    path('',views.school,name='school'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),

]