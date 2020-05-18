from django.urls import path
from . import views

# 누군가 해당 웹사이트에 들어왔을 때 views.post_list를 보여주라고 말함
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
