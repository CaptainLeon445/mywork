from django.urls import path
from fifth_app import views


app_name='fifth_app'

urlpatterns=[
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),

]