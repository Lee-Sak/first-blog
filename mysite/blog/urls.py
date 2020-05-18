from django.urls import path
from . import views

# 누군가 해당 웹사이트에 들어왔을 때 views.post_list를 보여주라고 말함
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
