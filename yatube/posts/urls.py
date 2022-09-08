from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('group_list.html', views.group_list, name='group_list'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_posts'),
]
