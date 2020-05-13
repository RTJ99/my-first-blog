from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('sermon/', views.post_list, name='post_list'),
    path('about/', views.about_details, name='about'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

