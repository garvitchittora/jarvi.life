from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('todo', todo_page, name='todo_page'),
    path('login', login_page, name='login_page'),
]