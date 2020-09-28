from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<int:bug_id>', views.detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('login/register/',views.register_view, name='register'),
    path('newbug/', views.new_bug, name='newbug'),
]